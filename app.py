from config.api1_1_config import *
from config.netbox_config import *
from config.settings import *
from config.amqp import *
from modules.logger import Log
from modules.amqp import AMQPWorker
from modules.worker import WorkerThread, WorkerTasks
from netbox import ApidcimApi as Dcim
from netbox import Netbox
from on_http_api1_1 import NodesApi as Nodes
import argparse, sys, json, time, signal
import ssdp, requests, re

log = Log(__name__)
worker_info = {}
rackhd_info = {}
site_info = None

def get_data():
    return json.loads(config.api_client.last_response.data)

def nb_login(session):
    url = 'http://{0}:{1}/login/' \
        .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
    r = session.get(url)
    data = {}
    data['username'] = defaults.get('NETBOX_USER')
    data['password'] = defaults.get('NETBOX_PASS')
    data['csrfmiddlewaretoken'] = r.cookies['csrftoken']
    headers = {}
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['X-CSRFToken'] = r.cookies['csrftoken']
    r = session.post(url, data=data, headers=headers)
    r.raise_for_status()

def nb_create_site(site_name):
    Dcim().site_list_get()
    for site in get_data():
        if site.get('name') == site_name:
            log.debug('site ' + site_name + ' exists')
            return site
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/sites/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url)
        site_info = {
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
        r = session.post(url, data=site_info, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
    r.raise_for_status()
    Dcim().site_list_get()
    for site in get_data():
        if site.get('name') == site_name:
            log.debug(site, json=True)
            return site


def nb_add_device_role(role_name):
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
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/device-roles/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url) 
        role_data = {
            'color': color_map[type],
            'name': role_name,
            'slug': role_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new role for type ' + type)
        r = session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
    Dcim().device_role_list_get()
    for role in get_data():
        if role_name == role.get('name'):
            return role

def nb_add_device_type(mfg_name, model_name):
    Dcim().device_type_list_get()
    for type in get_data():
        if type_name == type.get('name'):
            return type
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/device-roles/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url)
        role_data = {
            'name': type_name,
            'slug': type_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new role for type ' + type)
        r = session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
    Dcim().device_type_list_get()
    for type in get_data():
        if type_name == type.get('name'):
            return type

def nb_add_device_mfg(mfg_name):
    Dcim().manufacturer_list_get()
    for mfg in get_data():
        if mfg_name == mfg.get('name'):
            return mfg
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/manufacturers/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url)
        mfg_data = {
            'name': mfg_name,
            'slug': mfg_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken']
        }
        log.info('creating new mfg for ' + mfg_name)
        r = session.post(url, data=role_data, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
    Dcim().manufacturer_list_get()
    for mfg in get_data():
        if mfg_name == mfg.get('name'):
            return mfg

def nb_add_rack(rack_srv):
    rack_name = re.search('uuid:(.*)::', rack_srv.usn).group(1)
    Dcim().rack_list_get()
    for rack in get_data():
        if rack.get('name') == rack_name:
            log.debug('rack ' + rack_name + ' exists')
            if not rack_name in rackhd_info:
                rackhd_info[rack_name] = rack_srv
            return rack
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/racks/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url)
        rack_info = {
            'name': rack_name,
            'u_height': '42',
            'width': '19',
            'site': site_info.get('id'), 
            'csrfmiddlewaretoken': r.cookies['csrftoken'],
            'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                .format(rack_srv.location, rack_srv.usn)
        }
        log.info('creating rack ' + rack_name)
        r = session.post(url, data=rack_info, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
    Dcim().rack_list_get()
    for rack in get_data():
        if rack.get('name') == rack_name:
            rackhd_info[rack_name] = rack_srv
            return rack

def nb_add_device(device_name):
    Dcim().device_list_get()
    for device in get_data():
        if device.get('name') == device_name:
            log.debug('node ' + device_name + ' exists')
            return device
    with requests.session() as session:
        nb_login(session)
        url = 'http://{0}:{1}/dcim/nodes/add/' \
            .format(defaults.get('NETBOX_HOST'), defaults.get('NETBOX_PORT'))
        r = session.get(url)
        device_info = {
            'name': device_name,
            'csrfmiddlewaretoken': r.cookies['csrftoken'],
            'comments': 'RackHD Service: \nlocation: {0} \nUSN: {1}' \
                .format(rack_srv.location, rack_srv.usn)
        }
        log.info('creating device ' + device_name)
        r = session.post(url, data=device_info, \
            headers={'Content-Type': 'application/x-www-form-urlencoded', \
                     'X-CSRFToken': r.cookies['csrftoken']})
        r.raise_for_status()
    Dcim().device_list_get()
    for device in get_data():
        if device.get('name') == device_name:
            return device


def shutdown(signum, stack):
    for key,val in worker_info.iteritems():
        val['worker'].stop()
    sys.exit(0)

def add_worker(worker, task, name):
    worker_info[name] = {
        'worker':worker, 
        'task':task
    }

def ssdp_listener():
    def start(ssdp,id):
        while worker_info[id]['task'].running == True:
            services = ssdp.discover("urn:schemas-upnp-org:service:api:1.1")
            if len(services) > 0:
                for srv in services:
                    if srv.usn not in rackhd_info:
                        log.debug('creating rack with location {0}'.format(srv.location))
                        nb_add_rack(srv)
            else:
                time.sleep(2)
    task = WorkerThread(ssdp,'ssdp')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'ssdp')
    worker.run()

def device_listener():
    def start(data, id):
        while worker_info[id]['task'].running == True:
            log.info('running device_listener')
            time.sleep(2)
    task = WorkerThread(None,'device_listener')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'device_listener')
    worker.run()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config/config.ini', required=False)
    parser.add_argument('--site', required=True)
    parser.add_argument('--loglevel', default='INFO', required=False)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    site_info = nb_create_site(args.site)
    signal.signal(signal.SIGINT, shutdown)
    ssdp_listener()
    device_listener()
    while True:
        time.sleep(5)

