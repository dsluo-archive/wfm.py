from dataclasses import dataclass
from datetime import datetime
from typing import List

from .abstract import Resource


@dataclass(init=False, frozen=True)
class Item(Resource):
    id: str
    url_name: str
    item_name: str
    thumb: str = None
    trading_tax: int = None
    tags: List[str] = None
    wiki_link: str = None
    description: str = None
    ducats: int = None
    icon: str = None
    icon_format: str = None
    sub_icon: str = None

    def _args(self):
        return [self.url_name]


@dataclass(init=False, frozen=True)
class Order(Resource):
    creation_date: datetime
    visible: bool
    quantity: int
    user: 'User'
    last_update: datetime
    platinum: int
    order_type: str
    region: str
    platform: str
    id: str
    item: Item

    def _args(self):
        return [self.url_name]


@dataclass(init=False, frozen=True)
class Statistics(Resource):
    type: str
    period: str
    volume: int
    min_price: int
    max_price: int
    avg_price: float
    wa_price: float
    median: int
    id: str
    item: Resource
    open_price: int = None
    closed_price: int = None
    moving_avg: float = None
    order_type: str = None
    timestamp: datetime = None
    donch_top: int = None
    donch_bot: int = None

    def _args(self):
        return [self.url_name]


@dataclass(init=False, frozen=True)
class Achievement(Resource):
    icon: str
    description: str
    name: str
    type: str
    exposed: bool


@dataclass(init=False, frozen=True)
class User(Resource):
    status: str
    about: str
    about_raw: str
    own_profile: bool
    last_seen: datetime
    reputation: int
    region: str
    achievements: List[Achievement]
    ingame_name: str
    background: str
    platform: str
    banned: bool
    id: str
    avatar: str


@dataclass(init=False, frozen=True)
class Review(Resource):
    user_from: User
    timestamp: datetime
    text: str
    id: str
    hidden: bool
    review_type: int


@dataclass(init=False, frozen=True)
class Ducat(Resource):
    pass
