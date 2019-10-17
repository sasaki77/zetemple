import pytest

from zetemple import zetemple


@pytest.fixture
def item_source():
    hosts = [{'name': 'host1', 'prefix': 'PREFIX1:'},
             {'name': 'host2', 'prefix': 'PREFIX2:'}]
    item_keys = ['zetemple.key1', 'zetemple.comma.KEY2', 'invalid.key']
    interval = 180
    func = 'ave'

    items = [
             {'host': 'host1', 'item_key': 'zetemple.key1',
                 'pv': 'PREFIX1:key1'},
             {'host': 'host1', 'item_key': 'zetemple.comma.KEY2',
                 'pv': 'PREFIX1:KEY2'},
             {'host': 'host2', 'item_key': 'zetemple.key1',
                 'pv': 'PREFIX2:key1'},
             {'host': 'host2', 'item_key': 'zetemple.comma.KEY2',
                 'pv': 'PREFIX2:KEY2'},
            ]

    for item in items:
        item['func'] = func
        item['interval'] = interval

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


@pytest.mark.parametrize('key,pvname', [
    ('zetemple.key1', 'key1'),
    ('zetemple.comma.KEY2', 'KEY2'),
    ('zetemple.comma.pv.KEY.FIELD', 'KEY.FIELD'),
    ('zetemple.comma.pv', 'pv'),
    ('ZETEMPLE.comma.pv', 'pv'),
    ('key1', None)
])
def test_parse_item_key(key, pvname):
    _pvname = zetemple.__parse_item_key(key)
    assert pvname == _pvname
