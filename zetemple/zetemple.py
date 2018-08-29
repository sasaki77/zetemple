import argparse
import os

from zbxepics import ZabbixSenderCA
from zbxepics.logging import logger

from .reader import SenderConfigReaderCSV
from .zbxsenderapi import ZabbixSenderAPI


def create_items(hosts, item_keys, interval, func=None):
    items = []

    for host in hosts:
        hostname = host['name']
        prefix = host['prefix']
        for item_key in item_keys:
            item = {}
            item['host'] = hostname
            item['item_key'] = item_key
            lastname = item_key.split('.')[-1]
            item['pv'] = ':'.join([prefix, lastname.upper()])
            item['interval'] = interval
            item['func'] = func
            items.append(item)

    return items


def parseArgs():
    default_server = 'localhost'
    default_port = 10051
    default_interval = 30
    default_function = 'last'
    default_zbxurl = 'http://localhost/zabbix'
    default_zbxuser = 'Admin'
    default_zbxpass = 'zabbix'

    dir_path = os.path.dirname(__file__)
    default_logcnf = os.path.join(dir_path, 'logging.conf')

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '-file', dest="file",
                        required=True, help='CSV file')
    parser.add_argument('-s', '--server', dest='server',
                        default=default_server,
                        help='Zabbix server ip address.',
                        metavar=default_server)
    parser.add_argument('-t', '--template', dest='template',
                        required=True, help='Zabbix template name.',
                        metavar='PASSWORD')
    parser.add_argument('-p', '--port', dest="port",
                        default=default_port, type=int,
                        help='Zabbix server port.', metavar=default_port)
    parser.add_argument('-i', '--interval', dest='interval',
                        default=default_interval, type=float,
                        help='Sender interval.', metavar=default_interval)
    parser.add_argument('-F', '--function', dest='function',
                        default=default_function,
                        help='Sender Function. Default:',
                        metavar=default_function)
    parser.add_argument('-u', '--zbx_url', dest='zbx_url',
                        help='URL to zabbix api.',
                        default=default_zbxurl, metavar='URL')
    parser.add_argument('-U', '--zbx_user', dest='zbx_user',
                        help='Zabbix user name.', default=default_zbxuser,
                        metavar='USER')
    parser.add_argument('-P', '--zbx_password', dest='zbx_password',
                        help='Zabbix user password.', default=default_zbxpass,
                        metavar='PASSWORD')
    parser.add_argument('-l', '--logconfig', dest='logconfig',
                        help='logging config file path.',
                        default=default_logcnf)

    return parser.parse_args()


def main():
    args = parseArgs()

    logger.set_config(args.logconfig)

    csv_reader = SenderConfigReaderCSV()
    hosts = csv_reader.read_config(args.file)

    zbx_url = args.zbx_url
    zbx_user = args.zbx_user
    zbx_password = args.zbx_password
    sender_api = ZabbixSenderAPI(zbx_url, zbx_user, zbx_password)

    template_name = args.template
    template_items = sender_api.get_items_by_template(template_name)

    item_keys = []
    for item in template_items:
        item_keys.append(item['key_'])

    items = create_items(hosts, item_keys, args.interval, args.function)
    try:
        sender = ZabbixSenderCA(args.server, args.port, items=items)
        sender.run()
    except KeyboardInterrupt:
        pass
    finally:
        sender.stop()


if __name__ == '__main__':
    main()
