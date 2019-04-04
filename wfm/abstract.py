import abc
import dataclasses
from typing import Type, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client


class Endpoint(abc.ABC):
    path: str = NotImplemented
    resource: Type['Resource'] = NotImplemented

    def __init__(self, client: 'Client', children: Dict[str, 'Endpoint'] = None):
        self.client = client
        self.children = children

    def _get(self, *args, **kwargs) -> resource:
        response = self.client._get(self.path.format(*args), **kwargs)
        return self._build_resource(response)

    @abc.abstractmethod
    def _build_resource(self, response) -> resource:
        raise NotImplementedError

    def __call__(self, *args, **kwargs) -> resource:
        return self._get(*args, **kwargs)


@dataclasses.dataclass(init=False)
class Resource:
    def __init__(self, endpoint):
        self.endpoint: Endpoint = endpoint
        for name, child in self.endpoint.children.items():
            setattr(self, name, child.__call__)
