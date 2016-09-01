from config.settings import *
from config.amqp import *
from modules.logger import Log
from modules.amqp import AMQPWorker
from modules.worker import WorkerThread, WorkerTasks
from netbox import Netbox
from on_http_api1_1 import NodesApi as Nodes
import argparse, sys, json, time, signal
import ssdp, requests, re, copy
from sets import Set

log = Log(__name__)
worker_info = {}

def shutdown(signum, stack):
    for key,val in worker_info.iteritems():
        val['worker'].stop()
    sys.exit(0)

def add_worker(worker, task, name):
    worker_info[name] = {
        'worker':worker, 
        'task':task
    }

def ssdp_listener(nb):
    def start(ssdp,id):
        while worker_info[id]['task'].running == True:
            services = ssdp.discover("urn:schemas-upnp-org:service:api:1.1")
            if len(services) > 0:
                for srv in services:
                    nb.nb_add_rack(srv)
            time.sleep(5)
    task = WorkerThread(ssdp,'ssdp')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'ssdp')
    worker.run()

def rack_device_init(rack_srv):
    url = rack_srv.location
    log.info('initializing new rack @ ' + url)
    r = requests.get(url + 'nodes/')
    log.info(r.json(), json=True)
    return r
    
def rack_device_listener(nb):
    def start(data, id):
        last_rack_set = {}
        while worker_info[id]['task'].running == True:
            current_rack_set = nb.rack_info()
            new_rack_set = Set(current_rack_set.keys()) - Set(last_rack_set.keys())
            if len(new_rack_set) > 0:
                for rack_srv in new_rack_set:
                    rack_device_init(current_rack_set[rack_srv])   
                last_rack_set = copy.deepcopy(current_rack_set)
            time.sleep(2)
    task = WorkerThread(None,'device_listener')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'device_listener')
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
    ssdp_listener(nb)
    rack_device_listener(nb)
    signal.signal(signal.SIGINT, shutdown)
    signal.pause()
