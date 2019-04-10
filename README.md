# wfm.py

A library for Warframe Market

## Requirements

* Python 3.7+
* `requests`

## Usage

Get the list of all items.
```python
from wfm import Client
from pprint import pprint

c = Client()
items = c.items()

pprint(items)
```
```
[Item(item_name="Scindo Prime Handle"),
 Item(item_name="Ember Prime Neuroptics"),
 Item(item_name="Loki Prime Blueprint"),
 Item(item_name="Ember Prime Chassis"),
 Item(item_name="Hammer Shot"),
 Item(item_name="Seeking Force"),
 Item(item_name="Target Cracker"),
 Item(item_name="Fleeting Expertise"),
 Item(item_name="Critical Delay"),
 ...
]
```

Get orders for the Scindo Prime Handle.
```python
handle = items[0]
pprint(handle.orders())
```
```
[Order(endpoint=<wfm.endpoints.OrdersEndpoint object at 0x000001EB08C932E8>, creation_date=datetime.datetime(2016, 8, 3, 7, 3, 35, tzinfo=datetime.timezone.utc), visible=True, quantity=99, user={'ingame_name': 'Mastarius', 'last_seen': '2019-04-09T21:16:09.349+00:00', 'reputation_bonus': 0, 'reputation': 9, 'region': 'en', 'status': 'offline', 'id': '57a19114d3ffb639d23d35c4', 'avatar': None}, last_update=datetime.datetime(2018, 1, 9, 2, 19, 33, tzinfo=datetime.timezone.utc), platinum=2, order_type='buy', region='en', platform='pc', id='57a197470f31393be0684915', item=Item(item_name="Scindo Prime Handle")),
 Order(endpoint=<wfm.endpoints.OrdersEndpoint object at 0x000001EB08C932E8>, creation_date=datetime.datetime(2016, 11, 26, 11, 5, 42, tzinfo=datetime.timezone.utc), visible=True, quantity=5, user={'ingame_name': '-SW-KOJOT', 'last_seen': '2019-04-09T20:09:00.444+00:00', 'reputation_bonus': 0, 'reputation': 6, 'region': 'en', 'status': 'offline', 'id': '57a6f107d3ffb64144f02c36', 'avatar': None}, last_update=datetime.datetime(2019, 4, 4, 8, 17, tzinfo=datetime.timezone.utc), platinum=12, order_type='sell', region='en', platform='pc', id='58396c860f31390b0409eca5', item=Item(item_name="Scindo Prime Handle")),
 ...
]
```

## TODO

* unit testing
* documentation
* implementation for profile endpoints
* publish on pypi
* rate limiting
* cache where appropriate
