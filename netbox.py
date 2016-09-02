from config.netbox_config import *
from modules.logger import Log
from modules.worker import WorkerThread, WorkerTasks
from netbox_rest import ApidcimApi as Dcim
from netbox_rest import ApicircuitsApi as Circuit
from netbox_rest import ApiipamApi as Ipam
from netbox_rest import ApisecretsApi as Secret
from netbox_rest import ApitenancyApi as Tenancy
import sys, json, time
import requests, re

log = Log(__name__)
ROLE_COLOR_MAP = {
    'compute': 'blue',
    'switch': 'green',
    'enclosure': 'orange',
    'pdu': 'red'
}
def sanitize_slug(str):
    for c in ['.','#','+','?','$','%','!','@','\\','/','\"']:
        str = str.replace(c, '')
    return str.replace(' ', '-').lower()

class Netbox(object):
    def __init__(self, *args, **kwargs):
        # create session and login
        self.__session = requests.session()
        self.__base_url = 'http://{0}:{1}'.format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        self.__nb_login()
        self.__rack_info = {}
        self.__api_client = config.api_client
        self.__site_info = self.nb_create_site(args[0])

    def __get_data(self):
        return json.loads(self.__api_client.last_response.data)
        
    def __post(self, path, data=None):
        r = self.__get(path)
        if isinstance(data, dict):
            data['csrfmiddlewaretoken'] = r.cookies['csrftoken']
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': r.cookies['csrftoken']
        }
        url = '{0}/{1}'.format(self.__base_url, path)
        r = self.__session.post(url, data=data, headers=headers)
        r.raise_for_status()
        return r
            
    def __get(self, path):
        r = self.__session.get('{0}/{1}'.format(self.__base_url, path))
        r.raise_for_status()
        return r
            
    def __nb_login(self):
        data = {}
        data['username'] = defaults.get('NETBOX_USER')
        data['password'] = defaults.get('NETBOX_PASS')
        self.__post('/login/', data=data)

    def nb_create_site(self, opts):
        site_name = opts.site
        Dcim().site_list_get()
        for site in self.__get_data():
            if site.get('name') == site_name:
                log.info('site ' + site_name + ' exists')
                return site
        site_data = {
            'name': site_name,
            'slug': opts.slug,
            'asn': opts.asn if opts.asn != None else '',
            'comments': opts.comments if opts.comments != None else '',
            'facility': opts.facility if opts.facility != None else '',
            'physical_address': opts.physical if opts.physical != None else '',
            'shipping_address': opts.shipping if opts.shipping != None else '',
            'tenant': opts.tenant if opts.tenant != None else '',
        }
        if site_data['slug'] == None:
            site_data['slug'] = sanitize_slug(site_name)
        log.info('creating site ' + site_name)
        self.__post('/dcim/sites/add/', data=site_data)
        Dcim().site_list_get()
        for site in self.__get_data():
            if site.get('name') == site_name:
                self.__site_info = site
                log.debug(self.__site_info, json=True)
                return site

    def nb_add_rack(self, rack_srv):
        rack_name = re.search('uuid:(.*)::', rack_srv.usn).group(1)
        if rack_name in self.__rack_info:
            return
        log.debug('creating rack with location {0}'.format(rack_srv.location))
        Dcim().rack_list_get_0(self.__site_info.get('id'))
        add_rack = True
        for rack in self.__get_data():
            if rack.get('name') == rack_name:
                log.debug('rack ' + rack_name + ' exists')
                add_rack = False
        if add_rack:
            rack_info = {
                'name': rack_name,
                'u_height': '42',
                'width': '19',
                'site': self.__site_info.get('id'), 
                'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                    .format(rack_srv.location, rack_srv.usn)
            }
            log.info('creating rack ' + rack_name)
            self.__post('/dcim/racks/add/', data=rack_info)
        Dcim().rack_list_get()
        for rack in self.__get_data():
            if rack.get('name') == rack_name:
                self.__rack_info[rack_name] = rack_srv
                return rack

    def nb_add_device_role(self, type):
        Dcim().device_role_list_get()
        for role in self.__get_data():
            if type == role.get('name'):
                log.debug('role ' + type + ' exists')
                return role
        role_data = {
            'color': ROLE_COLOR_MAP[type],
            'name': type,
            'slug': sanitize_slug(type)
        }
        log.info('creating new role for type ' + type)
        self.__post('/dcim/device-roles/add/', data=role_data)
        Dcim().device_role_list_get()
        for role in self.__get_data():
            if type == role.get('name'):
                return role

    def nb_add_device_type(self, **kwargs):
        mfg_name = kwargs.get('mfg_name')
        model = kwargs.get('model')
        height = kwargs.get('height')
        length = kwargs.get('length')
        type = kwargs.get('type')
        pn = kwargs.get('pn')
        Dcim().device_type_list_get()
        for type in self.__get_data():
            if mfg_name == type.get('manufacturer') and \
               model == type.get('model') and \
               pn == type('part_number'):
                return type
        Dcim().manufacturer_list_get()
        for mfg in self.__get_data():
            if mfg_name == mfg.get('name'):
                try: # create a valid unit height 
                    val = [int(s) for s in height.split() if s.isdigit()]
                    height = int(height[0])
                except ValueError, IndexError:
                    log.warning('unit height: ' + height)
                    height = 1
                type_data = {
                    'manufacturer': mfg.get('id'),
                    'part_number': pn,
                    'model': model,
                    'slug': sanitize_slug(model),
                    'u_height': height
                }
                if type == 'switch':
                    type_data['is_network_device'] = 'on'
                if length != 'Short': 
                    type_data['is_full_depth'] = 'on'
                log.info('creating device type for model: {0}, sku: {1}, mfg: {2}' \
                    .format(model, pn, mfg_name))
                r = self.__post('/dcim/device-types/add/', data=type_data)
        Dcim().device_type_list_get()
        for type in self.__get_data():
            if mfg_name == type.get('manufacturer'):
                return type

    def nb_add_device_mfg(self, mfg_name):
        Dcim().manufacturer_list_get()
        for mfg in self.__get_data():
            if mfg_name == mfg.get('name'):
                log.debug('manufacturer ' + mfg_name + ' exists')
                return mfg
        mfg_data = {
            'name': mfg_name,
            'slug': sanitize_slug(mfg_name)
        }
        log.info('creating new mfg for ' + mfg_name)
        r = self.__post('/dcim/manufacturers/add/', data=mfg_data)
        Dcim().manufacturer_list_get()
        for mfg in self.__get_data():
            if mfg_name == mfg.get('name'):
                return mfg

    def nb_add_device(self, device_name):
        Dcim().device_list_get()
        for device in self.__get_data():
            if device.get('name') == device_name:
                log.debug('node ' + device_name + ' exists')
                return device
        device_info = {
            'name': device_name,
            'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                .format(rack_srv.location, rack_srv.usn)
        }
        log.info('creating device ' + device_name)
        r = self.__post('/dcim/nodes/add/', data=device_info)
        Dcim().device_list_get()
        for device in self.__get_data():
            if device.get('name') == device_name:
                return device

    def rack_info(self):
        return self.__rack_info
        
    def site_info(self):
        return self._site_info
