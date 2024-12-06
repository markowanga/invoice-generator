from typing import Any, Dict

from jinja2 import Template

from invoice_generator.application.resource_provider import ResourceProvider
from invoice_generator.application.template_renderer import TemplateRenderer


class Jinja2TemplateRenderer(TemplateRenderer):
    _resource_provider: ResourceProvider

    def __init__(self, resource_provider: ResourceProvider):
        self._resource_provider = resource_provider

    def render(self, template_file: str, input_dict: Dict[str, Any]) -> str:
        return Template(self._resource_provider.get_resource(template_file)).render(
            input_dict
        )
