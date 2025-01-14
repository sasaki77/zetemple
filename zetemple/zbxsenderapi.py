from zabbix_utils import ZabbixAPI


class ZabbixSenderAPI(object):

    def __init__(self, url=None, user=None, password=None):
        self.api = ZabbixAPI(url=url)
        self.user = user
        self.password = password

    def get_items_by_template(self, template_name):
        self.api.login(user=self.user, password=self.password)

        items = self.api.item.get(
            output=['itemid', 'name', 'key_'], filter={'key_': None, 'host': template_name}
        )

        self.api.logout()

        return items
