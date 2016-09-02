import logging
import os, sys
import ConfigParser

CONFIG = 'config/config.ini'
for v in sys.argv:
    if 'config' in v:
        CONFIG = v.split('=')[1:]
config_parser = ConfigParser.RawConfigParser()
config_parser.read(CONFIG)
defaults = {}
for k,v in config_parser.items('DEFAULT'):
    defaults[k.upper()] = v

NETBOX_HOST = defaults['NETBOX_HOST']
NETBOX_PORT = defaults['NETBOX_PORT']
NETBOX_PORT_AUTH = defaults['NETBOX_PORT_AUTH']
NETBOX_VERIFY_SSL = defaults['NETBOX_VERIFY_SSL']
NETBOX_USER = defaults['NETBOX_USER']
NETBOX_PASS = defaults['NETBOX_PASS']
NETBOX_PASS = defaults['NETBOX_PASS']
NETBOX_DEBUG = defaults['NETBOX_DEBUG']

# Global logger setup: CRITICAL < ERROR < WARNING < INFO < DEBUG
LOGFORMAT = '%(asctime)s:%(name)s:%(levelname)s - %(message)s'
LOGLEVELS = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}
LOGGER_LVL = defaults['LOGLEVEL']
logging.basicConfig(level=LOGLEVELS[LOGGER_LVL], format=LOGFORMAT)
