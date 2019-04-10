# wfm.py

A library for Warframe Market

## Requirements

* Python 3.7+
* `requests`

## Usage

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

## TODO

* unit testing
* documentation
* implementation for profile endpoints
* publish on pypi
