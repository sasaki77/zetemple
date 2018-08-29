from pyzabbix import ZabbixAPI

from zbxepics.zbxconfig.apiobjects import Item


class ZabbixSenderAPI(object):

    def __init__(self, url=None, user=None, password=None):
        self._zbx_api = ZabbixAPI(url=url, user=user, password=password)
        self.__item = Item(self._zbx_api, templated=True)

    def get_items_by_template(self, template_name):
        items = self.__item.get_items_by_key(None, template_name)
        return items
