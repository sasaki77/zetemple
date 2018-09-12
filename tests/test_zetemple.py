import pytest

from zetemple import zetemple


@pytest.fixture
def item_source():
    hosts = [{"name": "host1", "prefix": "PREFIX1:"},
             {"name": "host2", "prefix": "PREFIX2:"}]
    item_keys = ["key1", "commma.KEY2"]
    interval = 180
    func = "ave"
    items = [
             {'host': 'host1', 'item_key': 'key1', 'pv': 'PREFIX1:key1',
              'interval': 180, 'func': 'ave'},
             {'host': 'host1', 'item_key': 'commma.KEY2', 'pv': 'PREFIX1:KEY2',
              'interval': 180, 'func': 'ave'},
             {'host': 'host2', 'item_key': 'key1', 'pv': 'PREFIX2:key1',
              'interval': 180, 'func': 'ave'},
             {'host': 'host2', 'item_key': 'commma.KEY2', 'pv': 'PREFIX2:KEY2',
              'interval': 180, 'func': 'ave'},
            ]
    source = {'hosts': hosts, 'item_keys': item_keys,
              'interval': interval, 'func': func,
              'items': items}
    return source


def test_create_items(item_source):
    hosts = item_source['hosts']
    item_keys = item_source['item_keys']
    interval = item_source['interval']
    func = item_source['func']

    items = zetemple.create_items(hosts, item_keys, interval, func)

    assert items == item_source['items']
