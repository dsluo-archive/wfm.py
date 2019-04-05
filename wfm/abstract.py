import abc
import dataclasses
from typing import Type, Dict, TYPE_CHECKING, Union, List

if TYPE_CHECKING:
    from .client import Client


@dataclasses.dataclass(frozen=True)
class Resource:
    endpoint: 'Endpoint'

    def __post_init__(self):
        for name, child in self.endpoint.children.items():
            setattr(self, name, child.__call__)


class Endpoint(abc.ABC):
    path: str = NotImplemented
    resource: Type[Resource] = Resource

    def __init__(self, client: 'Client', children: Dict[str, 'Endpoint'] = None):
        self.client = client
        self.children = children or {}

    def _get(self, *args, **kwargs) -> Union[resource, List[resource]]:
        response = self.client._get(self.path.format(*args), **kwargs)
        return self._build_resource(response)

    @abc.abstractmethod
    def _build_resource(self, payload) -> Union[resource, List[resource]]:
        raise NotImplementedError

    def __call__(self, *args, **kwargs) -> Union[resource, List[resource]]:
        return self._get(*args, **kwargs)
