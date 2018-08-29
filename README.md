# Zabbix epics template sender
This package provide executable script to send metrics to Zabbix server from EPICS records via ChannelAccess.

PV names are obtained from template of Zabbix to monitor EPICS PVs.

The Item key of Zabbix template are must be PV name or last part of comma separated key as follow.

ex.1) `PV:name`

ex.2) `comma.separated.PV:name`

## installing

Simple install is below.

```bash
pip install git+https://github.com/sasaki77/zabbix-epics-py.git
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
```
