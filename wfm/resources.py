from dataclasses import dataclass
from typing import List

from .abstract import Resource


@dataclass(frozen=True)
class Item(Resource):
    url_name: str
    id: str
    item_name: str
    tags: List[str] = None
    thumb: str = None

@dataclass(frozen=True)
class Order(Resource):
    pass

@dataclass(frozen=True)
class Statistics(Resource):
    pass

@dataclass(frozen=True)
class Profile(Resource):
    pass

@dataclass(frozen=True)
class Review(Resource):
    pass

@dataclass(frozen=True)
class Ducat(Resource):
    pass