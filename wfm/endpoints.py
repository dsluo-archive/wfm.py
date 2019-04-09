from typing import Union, List

from .abstract import Endpoint
from .resources import Item, Order, Statistics, User, Review, Ducat


class ItemsEndpoint(Endpoint):
    path = '/items'
    resource = Item

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        # noinspection PyArgumentList
        return [self.resource(self, **item) for item in payload['items'][self.client.language]]


class ItemEndpoint(Endpoint):
    path = '/items/{}'
    resource = Item

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        # noinspection PyArgumentList
        return [
            self.resource(
                self,
                **item.pop(self.client.language),
                **item
            ) for item in payload['item']['items_in_set']
        ]


class OrdersEndpoint(Endpoint):
    path = '/items/{}/orders'
    resource = Order

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        # noinspection PyArgumentList
        return [self.resource(self, item=parent_resource, **order) for order in payload['orders']]


class StatisticsEndpoint(Endpoint):
    path = '/items/{}/statistics'
    resource = Statistics

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        # noinspection PyArgumentList
        return [
                   self.resource(
                       self,
                       timestamp=stat.pop('datetime', None),
                       type='closed',
                       period='48hours',
                       item=parent_resource,
                       **stat
                   ) for stat in payload['statistics_closed']['48hours']
               ] + [
                   self.resource(
                       self,
                       timestamp=stat.pop('datetime', None),
                       type='closed',
                       period='90days',
                       item=parent_resource,
                       **stat
                   ) for stat in payload['statistics_closed']['90days']
               ] + [
                   self.resource(
                       self,
                       timestamp=stat.pop('datetime', None),
                       type='live',
                       period='48hours',
                       item=parent_resource,
                       **stat
                   ) for stat in payload['statistics_live']['48hours']
               ] + [
                   self.resource(
                       self,
                       timestamp=stat.pop('datetime', None),
                       type='live',
                       period='90days',
                       item=parent_resource,
                       **stat
                   ) for stat in payload['statistics_live']['90days']
               ]


class ProfileEndpoint(Endpoint):
    path = '/profile/{}'
    resource = User

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        pass


class ProfileOrdersEndpoint(Endpoint):
    path = '/profile/{}/orders'
    resource = Order

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        pass


class ProfileStatisticsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Statistics

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        pass


class ProfileReviewsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Review

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        pass


class DucatsEndpoint(Endpoint):
    path = '/tools/ducats'
    resource = Ducat

    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        pass
