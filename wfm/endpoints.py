from .abstract import Endpoint
from .resources import Item, Order, Statistics, Profile, Review, Ducat


class ItemsEndpoint(Endpoint):
    path = '/items'
    resource = Item


class ItemEndpoint(Endpoint):
    path = '/items/{}'
    resource = Item


class OrdersEndpoint(Endpoint):
    path = '/items/{}/orders'
    resource = Order


class StatisticsEndpoint(Endpoint):
    path = '/items/{}/statistics'
    resource = Statistics


class ProfileEndpoint(Endpoint):
    path = '/profile/{}'
    resource = Profile


class ProfileOrdersEndpoint(Endpoint):
    path = '/profile/{}/orders'
    resource = Order


class ProfileStatisticsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Statistics


class ProfileReviewsEndpoint(Endpoint):
    path = '/profile/{}/statistics'
    resource = Review


class DucatsEndpoint(Endpoint):
    path = '/tools/ducats'
    resource = Ducat
