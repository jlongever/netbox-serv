from config.settings import *
from config.amqp import *
from modules.logger import Log
from modules.amqp import AMQPWorker
from modules.worker import WorkerThread, WorkerTasks
from netbox import Netbox
import argparse, sys, json, time, signal
import ssdp, requests, re, copy
from sets import Set
from urlparse import urlparse

log = Log(__name__)
worker_info = {}
amqp_info = {}

def shutdown(signum, stack):
    for key,val in amqp_info.iteritems():
        log.info('stopping ' + key)
        val['amqp'].stop()
    for key,val in worker_info.iteritems():
        val['worker'].stop()
    sys.exit(0)

def add_amqp_listener(amqp, name):
    amqp_info[name] = {
        'amqp':amqp
    }

def add_worker(worker, task, name):
    worker_info[name] = {
        'worker':worker, 
        'task':task
    }
    
def add_rack_node(nb, node, rack_srv):
    if 'type' in node and 'id' in node:
        type = node.get('type')
        id = node.get('id')
        log.info('[{0}]: adding node {1}'.format(rack_srv.location, id))
        dev_role = nb.nb_add_device_role(type)
        if type == 'compute':
            r = requests.get(rack_srv.location + 'nodes/' + id + '/catalogs/ohai')
            ohai = r.json().get('data', None)
            if ohai != None:
                mfg_name = ohai['dmi']['system'].get('manufacturer', 'unknown')
                model = ohai['dmi']['system'].get('product_name', 'unknown')
                sku = ohai['dmi']['system'].get('sku_number', 'unknown')
                length = ohai['dmi']['chassis'].get('length', 'unknown')
                height = ohai['dmi']['chassis'].get('height', 'unknown')
                dev_mfg = nb.nb_add_device_mfg(mfg_name)
                dev_type = nb.nb_add_device_type(mfg_name=mfg_name, \
                    model=model, pn=sku, height=height, length=length, type=type)
                dev = nb.nb_add_device(device_role=dev_role, \
                    device_type=dev_type, device_mfg=dev_mfg, rack_srv=rack_srv)
        if type == 'switch':
            r = requests.get(rack_srv.location + 'nodes/' + id + '/catalogs/snmp-1')
            snmp = r.json().get('data', None)
            if any(key.startswith('ENTITY-MIB') for key in snmp):
                mfg_name = snmp['ENTITY-MIB::entPhysicalMfgName_10']
                model = snmp['ENTITY-MIB::entPhysicalModelName_10']
                dev_mfg = nb.nb_add_device_mfg(mfg_name)
                dev_type = nb.nb_add_device_type(mfg_name=mfg_name, \
                    model=model, pn=model, height='1', length='Short', type=type)
                dev = nb.nb_add_device(device_role=dev_role, \
                    device_type=dev_type, device_mfg=dev_mfg, rack_srv=rack_srv)
        if type == 'pdu':
            pass    

def service_listener(nb):
    def start(ssdp, id):
        while worker_info[id]['task'].running == True:
            services = ssdp.discover("urn:schemas-upnp-org:service:api:1.1")
            if len(services) > 0:
                for srv in services:
                    nb.nb_add_rack(srv)
            time.sleep(5)
    task = WorkerThread(ssdp, 'service_listener')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker, task, 'service_listener')
    worker.run()

def device_listener(nb, rack_srv):
    url_parsed = urlparse(rack_srv.location)
    amqp_url = url_parsed.netloc.split(':')[0] 
    id = 'amqp.{0}'.format(amqp_url)
    def start(data, id):
        log.info('starting amqp listener @' + id)
        amqp = AMQPWorker(amqp_url=amqp_url, queue=QUEUE_GRAPH_FINISH, callbacks=[handler_cb])
        add_amqp_listener(amqp, id)
        amqp.start()
            
    def handler_cb(body, message):
        r = requests.get(rack_srv.location + 'workflows')
        workflows = r.json()
        for work in workflows:
            definition = work.get('definition', {})
            injectableName = definition.get('injectableName')
            if injectableName == 'Graph.SKU.Discovery':
                routeId = message.delivery_info.get('routing_key').split('graph.finished.')[1]
                graphId = work.get('context', {}).get('graphId')
                if graphId == routeId:
                    status = body.get('status')
                    if status == 'succeeded':
                        options = definition.get('options')
                        nodeid = options.get('defaults', {}).get('nodeId')
                        r = requests.get(rack_srv.location + 'nodes/' + nodeid)
                        add_rack_node(nb, r.json(), rack_srv)
                        message.ack()        
                        break
    
    task = WorkerThread(rack_srv, id)
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker, task, id)
    worker.run()    

def rack_listener(nb):
    def start(data, id):
        last_rack_set = {}
        while worker_info[id]['task'].running == True:
            current_rack_set = nb.rack_info()
            new_rack_set = Set(current_rack_set.keys()) - Set(last_rack_set.keys())
            if len(new_rack_set) > 0:
                for rack_srv in new_rack_set:
                    rack = current_rack_set[rack_srv]['service']
                    r = requests.get(rack.location + 'nodes/')
                    for node in r.json():
                        add_rack_node(nb, node, rack)
                    device_listener(nb, rack)  
                last_rack_set = copy.deepcopy(current_rack_set)
            time.sleep(2)
    task = WorkerThread(None,'rack_listener')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'rack_listener')
    worker.run()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config/config.ini', required=False)
    parser.add_argument('--site', required=True)
    parser.add_argument('--slug', required=False)
    parser.add_argument('--tenant', required=False)
    parser.add_argument('--facility', required=False)
    parser.add_argument('--asn', required=False)
    parser.add_argument('--physical', required=False)
    parser.add_argument('--shipping', required=False)
    parser.add_argument('--comments', required=False)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    options = parse_arguments()
    nb = Netbox(options)
    service_listener(nb)
    rack_listener(nb)
    signal.signal(signal.SIGINT, shutdown)
    signal.pause()
