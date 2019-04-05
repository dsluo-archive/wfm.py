from typing import Union, List

from .abstract import Endpoint
from .resources import Item, Order, Statistics, Profile, Review, Ducat


class ItemsEndpoint(Endpoint):
    path = '/items'
    resource = Item

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        return [self.resource(self, **item) for item in payload['items'][self.client.language]]


class ItemEndpoint(Endpoint):
    path = '/items/{}'
    resource = Item

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class OrdersEndpoint(Endpoint):
    path = '/items/{}/orders'
    resource = Order

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class StatisticsEndpoint(Endpoint):
    path = '/items/{}/statistics'
    resource = Statistics

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class ProfileEndpoint(Endpoint):
    path = '/profile/{}'
    resource = Profile

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class ProfileOrdersEndpoint(Endpoint):
    path = '/profile/{}/orders'
    resource = Order

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class ProfileStatisticsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Statistics

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class ProfileReviewsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Review

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass


class DucatsEndpoint(Endpoint):
    path = '/tools/ducats'
    resource = Ducat

    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        pass
