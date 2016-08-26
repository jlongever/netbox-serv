from settings import *
from on_http_api2_0 import Configuration, ApiClient

HOST_IP = RACKHD_HOST
HOST_PORT = RACKHD_HOST_PORT
HOST_PORT_AUTH = RACKHD_HOST_PORT_AUTH

config = Configuration()
config.host = 'http://{0}:{1}'.format(HOST_IP, HOST_PORT)
config.host_authed = 'https://{0}:{1}'.format(HOST_IP, HOST_PORT_AUTH)
config.api_root = '/api/2.0'
config.verify_ssl = False
config.api_client = ApiClient(host=config.host + config.api_root)
config.auth_enabled = False
config.debug = False
config.logger_format = LOGFORMAT
for key, elem in config.logger.iteritems():
    elem.setLevel(LOGLEVELS[LOGGER_LVL])



