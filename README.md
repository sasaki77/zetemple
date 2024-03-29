# Zabbix epics template sender
This package provides executable script to send metrics to Zabbix server from EPICS records via ChannelAccess.

PV names are obtained from template of Zabbix to monitor EPICS PVs.

The Item key of Zabbix template are must begin with "zetemple.". PV name must follow "zetemple." or last part of comma separated key as follow.

ex.1) `zetemple.PV:name`

ex.2) `zetemple.comma.separated.PV:name`

If the item key has `pv`, characters that follows `pv` are used as PV name.

ex.3) `zetemple.comma.separated.pv.PV:name.field`

## installing

Simple install is below.

```bash
pip install git+https://github.com/sasaki77/zetemple.git
```

Or clone this package and install it.

```bash
# clone the repository
git clone https://github.com/sasaki77/zetemple
cd zeteple
# install
pip install -r requirements.txt
pip install git+https://github.com/sasaki77/zetemple.git
```

## Usage

```bash
$ zetemple -h
usage: zetemple [-h] -f FILE [-s localhost] -t TEMPLATE [-p 10051] [-i 30] [-F last] [-u URL] [-U USER] [-P PASSWORD]
                [-l LOGCONFIG]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, -file FILE   CSV file
  -s localhost, --server localhost
                        Zabbix server ip address.
  -t TEMPLATE, --template TEMPLATE
                        Zabbix template name.
  -p 10051, --port 10051
                        Zabbix server port.
  -i 30, --interval 30  Sender interval.
  -F last, --function last
                        Sender Function. Default:
  -u URL, --zbx_url URL
                        URL to zabbix api.
  -U USER, --zbx_user USER
                        Zabbix user name.
  -P PASSWORD, --zbx_password PASSWORD
                        Zabbix user password.
  -l LOGCONFIG, --logconfig LOGCONFIG
                        logging config file path.
```

## Test

Install packages for develop
```bash
pip install -e .[develop]
```

Run without coverage:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov zetemple
coverage report -m
```
