from dataclasses import dataclass

from dynaconf import Dynaconf

from invoice_generator.domain.invoice import Invoice


@dataclass
class InvoiceConfig:
    file_version: str
    locale: str
    invoice: Invoice


def load_dynaconf(path: str) -> Dynaconf:
    return Dynaconf(settings_files=[path])


def load_config(path: str) -> InvoiceConfig:
    dynaconf = load_dynaconf(path)
    invoice_config = dynaconf['invoice_config']
    return InvoiceConfig(invoice_config['file_version'], invoice_config['locale'],
                         Invoice.from_dict(invoice_config['invoice']))

