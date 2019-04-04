from dataclasses import dataclass
from typing import List

from .abstract import Resource


@dataclass()
class Item(Resource):
    id: str
    url_name: str
    item_name: str
    tags: List[str]

@dataclass()
class Order(Resource):
    pass

@dataclass()
class Statistics(Resource):
    pass

@dataclass()
class Profile(Resource):
    pass

@dataclass()
class Review(Resource):
    pass

@dataclass()
class Ducat(Resource):
    pass