# netbox-serv

The netbox-serv project integrates RackHD hardware management and orchestration services with DigitalOcean's [netbox](https://github.com/digitalocean/netbox) DCIM/IPAM stack.

The netbox-serv runs as a per-site process- for each running service instance manages a site.

## Getting started

- Recommended to setup a virtual environment using python-virtualenv: 

```
virtual-env .venv
source .venv/bin/activate
```

- Install required python package dependencies: 

`pip install -r requirements.txt`

- To get program parameters run: 

`python app.py --help`

```
optional arguments:
  -h, --help           show this help message and exit
  --config CONFIG
  --site SITE
  --slug SLUG
  --tenant TENANT
  --facility FACILITY
  --asn ASN
  --physical PHYSICAL
  --shipping SHIPPING
  --comments COMMENTS
```

The `--site` argument is required.

- Start the service: `python app.py --site=<your site name>`

Netbox-serv will start, create a netbox site and discover all running RackHD services advertising on the network. 
For each RackHD service a corresponding netbox rack will be created. Each rack will be populated with existing nodes 
(switches, compute, pdu) and spawn AMQP listeners to listen/add new discovered nodes.

## Configuration

- Service options can be changed by modifying the `config/config.ini` (or specifying a custom config.ini using the `--config` option).

```
LOGLEVEL = WARNING
NETBOX_HOST = localhost
NETBOX_PORT = 80
NETBOX_PORT_AUTH = 443
NETBOX_USER = admin
NETBOX_PASS = admin
NETBOX_VERIFY_SSL = False
NETBOX_DEBUG = False
```

`python app.py --config=/home/me/myconfig.ini`


 
