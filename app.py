from config.api1_1_config import *
from config.settings import *
from config.amqp import *
from modules.logger import Log
from modules.amqp import AMQPWorker
from modules.worker import WorkerThread, WorkerTasks
from netbox import Netbox
from on_http_api1_1 import NodesApi as Nodes
import argparse, sys, json, time, signal
import ssdp, requests, re

log = Log(__name__)
worker_info = {}
nb = Netbox()

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
                    nb.nb_add_rack(srv)
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
    site_info = nb.nb_create_site(args.site)
    signal.signal(signal.SIGINT, shutdown)
    ssdp_listener()
    device_listener()
    while True:
        time.sleep(5)

