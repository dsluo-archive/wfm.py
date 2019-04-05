import requests

from .endpoints import OrdersEndpoint, StatisticsEndpoint, ItemEndpoint, ItemsEndpoint, ProfileOrdersEndpoint, \
    ProfileStatisticsEndpoint, ProfileReviewsEndpoint, ProfileEndpoint, DucatsEndpoint


class Client:
    BASE_ENDPOINT = 'https://api.warframe.market/v1'

    def __init__(self, session=None, language='en', platform='pc'):
        self.session = session or requests.Session()
        self.language = language
        self.platform = platform

        self.items = ItemsEndpoint(self)

        orders = OrdersEndpoint(self)
        stats = StatisticsEndpoint(self)
        self.item = ItemEndpoint(
            self,
            children={
                'orders': orders,
                'stats': stats
            }
        )

        profile_orders = ProfileOrdersEndpoint(self)
        profile_stats = ProfileStatisticsEndpoint(self)
        profile_reviews = ProfileReviewsEndpoint(self)

        self.profile = ProfileEndpoint(
            self,
            children={
                'orders':  profile_orders,
                'stats':   profile_stats,
                'reviews': profile_reviews
            }
        )

        # todo
        # self.ducats = DucatsEndpoint(self)

    def _request(self, method, endpoint, **kwargs):
        kwargs['headers'] = {
            'language': self.language,
            'platform': self.platform
        }

        response = self.session.request(method, self.BASE_ENDPOINT + endpoint, **kwargs)
        json = response.json()
        if response.status_code >= 400:
            json = json['error']
            raise ValueError('Error while querying API', response, json)

        try:
            json = json['payload']
        except KeyError:
            raise ValueError('Error while parsing API response', response, json)

        return json

    def _get(self, endpoint, **kwargs):
        return self._request('get', endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request('post', endpoint, **kwargs)

    def _put(self, endpoint, **kwargs):
        return self._request('put', endpoint, **kwargs)

    def _patch(self, endpoint, **kwargs):
        return self._request('patch', endpoint, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)
