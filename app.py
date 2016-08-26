from config.api1_1_config import *
from config.netbox_config import *
from config.amqp import *
from modules.logger import Log
from modules.amqp import AMQPWorker
from modules.worker import WorkerThread, WorkerTasks
from netbox import ApidcimApi as Dcim
import argparse, sys, json, time, signal
import ssdp

log = Log(__name__)
worker_info = {}
rackhd_info = {}

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
        while worker_info['ssdp']['task'].running == True:
            services = ssdp.discover("urn:schemas-upnp-org:service:api:1.1")
            if len(services) > 0:
                for srv in services:
                    if srv.usn not in rackhd_info:
                        log.debug('creating rack with location {0}'.format(srv.location))
                        rackhd_info[srv.usn] = srv
            else:
                time.sleep(2)
    task = WorkerThread(ssdp,'ssdp')
    worker = WorkerTasks(tasks=[task], func=start)
    add_worker(worker,task,'ssdp')
    worker.run()

def get_data():
    return json.loads(config.api_client.last_response.data)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config/config.ini', required=False)
    parser.add_argument('--loglevel', default='INFO', required=False)
    args = parser.parse_args()

if __name__ == '__main__':
    parse_arguments()
    signal.signal(signal.SIGINT, shutdown)
    Dcim().rack_list_get()
    log.info(get_data(), json=True)
    ssdp_listener()
    while True:
        time.sleep(5)

