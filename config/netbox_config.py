from settings import *
from netbox_rest import Configuration, ApiClient

config = Configuration()
config.username = NETBOX_USER
config.password = NETBOX_PASS
config.host = 'http://{0}:{1}'.format(NETBOX_HOST, NETBOX_PORT)
config.verify_ssl = True if NETBOX_VERIFY_SSL == "True" else False
config.debug = True if NETBOX_DEBUG == "True" else False
config.api_client = ApiClient(host=config.host)
config.logger_format = LOGFORMAT
for key, elem in config.logger.iteritems():
    elem.setLevel(LOGLEVELS[LOGGER_LVL])
