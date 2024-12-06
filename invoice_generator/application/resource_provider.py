from abc import ABC, abstractmethod


class ResourceProvider(ABC):
    @abstractmethod
    def get_resource(self, resource_file: str) -> str:
        pass
