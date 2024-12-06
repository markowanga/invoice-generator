import pkg_resources

from invoice_generator.application.resource_provider import ResourceProvider

_GENERATOR_PACKAGE_NAME = "invoice_generator"
_RESOURCES = "resources"


class PackageResourceProvider(ResourceProvider):
    def get_resource(self, resource_file: str) -> str:
        resource_path = "/".join((_RESOURCES, resource_file))
        return pkg_resources.resource_string(
            _GENERATOR_PACKAGE_NAME, resource_path
        ).decode("utf-8")
