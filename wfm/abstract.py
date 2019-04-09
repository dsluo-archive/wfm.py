import abc
import dataclasses
import functools
from dataclasses import dataclass
from datetime import datetime
from typing import Type, Dict, TYPE_CHECKING, Union, List

if TYPE_CHECKING:
    from .client import Client


@dataclass(init=False, frozen=True)
class Resource:
    endpoint: 'Endpoint'

    def __init__(self, endpoint, **attrs):
        object.__setattr__(self, 'endpoint', endpoint)

        for field in dataclasses.fields(self):
            if field.name == 'endpoint':
                continue
            try:
                value = attrs.pop(field.name, field.default)

                if value is dataclasses.MISSING:
                    raise KeyError
            except KeyError:
                raise TypeError(f'{field.name} is a required field.')

            try:
                parsed = datetime.fromisoformat(value)
                object.__setattr__(self, field.name, parsed)
                continue
            except (TypeError, ValueError):
                pass

            try:
                if issubclass(field.type, Resource):
                    if isinstance(value, Resource):
                        parsed = value
                    else:
                        parsed = field.type.endpoint._build_resource(self, value)
                    object.__setattr__(self, field.name, parsed)
                    continue
            except TypeError:
                pass

            object.__setattr__(self, field.name, value)

        object.__setattr__(self, '_extra', attrs)

    def _args(self):
        return []

    def _kwargs(self):
        return {}

    def __getattr__(self, item):
        if item == 'endpoint':
            return super(Resource, self).__getattribute__(self, item)
        try:
            child = self.endpoint.children[item]

            return functools.partial(child._get, self, *self._args(), **self._kwargs())
        except KeyError:
            raise AttributeError


class Endpoint(abc.ABC):
    path: str = NotImplemented
    resource: Type[Resource] = Resource

    def __init__(self, client: 'Client', children: Dict[str, 'Endpoint'] = None):
        self.client = client
        self.children = children or {}

    def _get(self, parent_resource, *args, **kwargs) -> Union[resource, List[resource]]:
        resource = self.client._get(self.path.format(*args), **kwargs)
        return self._build_resource(parent_resource, resource)

    @abc.abstractmethod
    def _build_resource(self, parent_resource, payload) -> Union[resource, List[resource]]:
        raise NotImplementedError

    def __call__(self, *args, **kwargs) -> Union[Resource, List[Resource]]:
        return self._get(None, *args, **kwargs)
