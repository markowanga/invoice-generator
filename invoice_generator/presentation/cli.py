import os.path

import typer
from typing_extensions import Annotated

from invoice_generator.application.invoice_details_processor import \
    InvoiceDetailsProcessor
from invoice_generator.application.value_formatter.europe_value_formatter import \
    EuropeValueFormatter
from invoice_generator.application.value_formatter.value_formatter import \
    ValueFormatter
from invoice_generator.infrastructure.jinja2_template_tenderer import \
    Jinja2TemplateRenderer
from invoice_generator.infrastructure.package_resource_provider import \
    PackageResourceProvider
from invoice_generator.infrastructure.pdfkit_pdf_generator import \
    PdfkitPdfGenerator
from invoice_generator.presentation.config_parser import load_config


def get_extension_with_dot_from_path(file_path: str) -> str:
    return os.path.splitext(file_path)[1]


def has_extension(file_path: str, extension_without_dot: str) -> bool:
    return get_extension_with_dot_from_path(file_path) == f".{extension_without_dot}"


def get_formatter(formatter_locale: str) -> ValueFormatter:
    if formatter_locale == "europe":
        return EuropeValueFormatter()
    else:
        raise Exception(f"Not found ValueFormatter with {formatter_locale} name")


app = typer.Typer()


@app.command()
def to_html(
    invoice_metadata: Annotated[
        str, typer.Option("-m", help="File with invoice details.")
    ],
    output_file: Annotated[str, typer.Option("-o", help="HTML file to save invoice.")],
) -> None:
    invoice_config = load_config(invoice_metadata)
    formatter = get_formatter(invoice_config.locale)
    processor = InvoiceDetailsProcessor(formatter)
    invoice_dict = processor.to_config(invoice_config.invoice)
    invoice_html = Jinja2TemplateRenderer(PackageResourceProvider()).render(
        template_file="template.html", input_dict=invoice_dict
    )
    with open(output_file, "w") as f:
        f.write(invoice_html)


@app.command()
def to_pdf(
    invoice_metadata: Annotated[
        str, typer.Option("-m", help="File with invoice details.")
    ],
    output_file: Annotated[str, typer.Option("-o", help="PDF file to save invoice.")],
) -> None:
    invoice_config = load_config(invoice_metadata)
    formatter = get_formatter(invoice_config.locale)
    processor = InvoiceDetailsProcessor(formatter)
    invoice_dict = processor.to_config(invoice_config.invoice)
    invoice_html = Jinja2TemplateRenderer(PackageResourceProvider()).render(
        template_file="template.html", input_dict=invoice_dict
    )
    PdfkitPdfGenerator().generate_pdf_from_string(invoice_html, output_file)


@app.command()
def example_yaml_config() -> None:
    print(PackageResourceProvider().get_resource("invoice_example.yaml"))


def main() -> None:
    app()
