from abc import ABC, abstractmethod
from typing import Any, Dict


class TemplateRenderer(ABC):

    @abstractmethod
    def render(self, template_name: str, input_dict: Dict[str, Any]) -> str:
        pass
