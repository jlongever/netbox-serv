from config.settings import *
from modules.logger import Log
from modules.worker import WorkerThread, WorkerTasks
from .apis.apicircuits_api import ApicircuitsApi as Circuit
from .apis.apidcim_api import ApidcimApi as Dcim
from .apis.apiipam_api import ApiipamApi as Ipam
from .apis.apisecrets_api import ApisecretsApi as Secret
from .apis.apitenancy_api import ApitenancyApi as Tenancy

import sys, json, time
import requests, re

log = Log(__name__)

class Netbox(object):
    def __init__(self, *args, **kwargs):
        self.__session = requests.session()
        self.__site_info = None
        self.__rack_info = {} 

    def __nb_login(self):
        url = 'http://{0}:{1}/login/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        data = {}
        data['username'] = defaults.get('NETBOX_USER')
        data['password'] = defaults.get('NETBOX_PASS')
        data['csrfmiddlewaretoken'] = r.cookies['csrftoken']
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['X-CSRFToken'] = r.cookies['csrftoken']
        r = self.__session.post(url, data=data, headers=headers)
        r.raise_for_status()

    def nb_create_site(self, site_name):
        Dcim().site_list_get()
        for site in get_data():
            if site.get('name') == site_name:
                log.debug('site ' + site_name + ' exists')
                return site
        url = 'http://{0}:{1}/dcim/sites/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        site_data = {
            '_create': '',
            'asn': '',
            'comments': '',
            'facility': '',
            'physical_address': '',
            'shipping_address': '',
            'tenant': '',
            'name': site_name,
            'slug': site_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating site ' + site_name)
        r = self.__session.post(url, data=site_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().site_list_get()
        for site in get_data():
            if site.get('name') == site_name:
                log.debug(site, json=True)
                return site


    def nb_add_device_role(self, role_name):
        colors_map = {
            'compute': 'blue',
            'switch': 'green',
            'enclosure': 'orange',
            'pdu': 'red'
        }
        Dcim().device_role_list_get()
        for role in get_data():
            if role_name == role.get('name'):
                return role
        url = 'http://{0}:{1}/dcim/device-roles/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url) 
        role_data = {
            'color': color_map[type],
            'name': role_name,
            'slug': role_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new role for type ' + type)
        r = self.__session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().device_role_list_get()
        for role in get_data():
            if role_name == role.get('name'):
                return role

    def nb_add_device_type(self, mfg_name, model_name):
        Dcim().device_type_list_get()
        for type in get_data():
            if type_name == type.get('name'):
                return type
        url = 'http://{0}:{1}/dcim/device-roles/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        role_data = {
            'name': type_name,
            'slug': type_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new role for type ' + type)
        r = self.__session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().device_type_list_get()
        for type in get_data():
            if type_name == type.get('name'):
                return type

    def nb_add_device_mfg(self, mfg_name):
        Dcim().manufacturer_list_get()
        for mfg in get_data():
            if mfg_name == mfg.get('name'):
                return mfg
        url = 'http://{0}:{1}/dcim/manufacturers/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        mfg_data = {
            'name': mfg_name,
            'slug': mfg_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new mfg for ' + mfg_name)
        r = self.__session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().manufacturer_list_get()
        for mfg in get_data():
            if mfg_name == mfg.get('name'):
                return mfg

    def nb_add_rack(self, rack_srv):
        rack_name = re.search('uuid:(.*)::', rack_srv.usn).group(1)
        Dcim().rack_list_get()
        for rack in get_data():
            if rack.get('name') == rack_name:
                log.debug('rack ' + rack_name + ' exists')
                if not rack_name in self.__rack_info:
                    self.__rack_info[rack_name] = rack_srv
                return rack
        url = 'http://{0}:{1}/dcim/racks/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        rack_info = {
            'name': rack_name,
            'u_height': '42',
            'width': '19',
            'site': self.__site_info.get('id'), 
            'csrfmiddlewaretoken': r.cookies['csrftoken'],
            'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                .format(rack_srv.location, rack_srv.usn)
        }
        log.info('creating rack ' + rack_name)
        r = self.__session.post(url, data=rack_info, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().rack_list_get()
        for rack in get_data():
            if rack.get('name') == rack_name:
                self.__rack_info[rack_name] = rack_srv
                return rack

    def nb_add_device(self, device_name):
        Dcim().device_list_get()
        for device in get_data():
            if device.get('name') == device_name:
                log.debug('node ' + device_name + ' exists')
                return device
        url = 'http://{0}:{1}/dcim/nodes/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = self.__session.get(url)
        device_info = {
            'name': device_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken'],
            'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                .format(rack_srv.location, rack_srv.usn)
        }
        log.info('creating device ' + device_name)
        r = self.__session.post(url, data=device_info, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
        Dcim().device_list_get()
        for device in get_data():
            if device.get('name') == device_name:
                return device

