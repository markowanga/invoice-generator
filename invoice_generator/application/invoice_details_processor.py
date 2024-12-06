from typing import Any, Dict

from invoice_generator.application.value_formatter.value_formatter import \
    ValueFormatter
from invoice_generator.domain.invoice import Invoice
from invoice_generator.domain.invoice_item import InvoiceItem


class InvoiceDetailsProcessor:
    _price_formatter: ValueFormatter

    def __init__(self, price_formatter: ValueFormatter):
        self._price_formatter = price_formatter

    def invoice_item_to_config(
        self, item: InvoiceItem, ordinal: int, currency: str
    ) -> Dict[str, Any]:
        return {
            "number": ordinal,
            "name": item.name,
            "unit": item.unit,
            "amount": self._price_formatter.format_value(item.amount),
            "item_price": self._price_formatter.format_price(
                item.net_single_price, currency
            ),
            "tax": f"{self._price_formatter.format_value(item.tax * 100)}%",
            "tax_value": self._price_formatter.format_price(
                item.count_total_tax(), currency
            ),
            "total_value": self._price_formatter.format_price(
                item.count_total_value(), currency
            ),
            "total_price_without_tax": self._price_formatter.format_price(
                item.count_total_value_without_tax(), currency
            ),
        }

    def to_config(self, invoice: Invoice) -> Dict[str, Any]:
        return {
            "document_number": invoice.document_number,
            "date_of_issue": self._price_formatter.format_date(invoice.date_of_issue),
            "sale_date": self._price_formatter.format_date(invoice.sale_date),
            "seller": invoice.seller,
            "buyer": invoice.buyer,
            "invoice_items": [
                self.invoice_item_to_config(
                    invoice.invoice_items[index], index + 1, invoice.currency
                )
                for index in range(len(invoice.invoice_items))
            ],
            "logo_url": invoice.logo_url,
            "account_number": invoice.account_number,
            "date_of_payment": self._price_formatter.format_date(
                invoice.sale_date.shift(days=invoice.days_for_pay)
            ),
            "total_invoice_value": self._price_formatter.format_price(
                sum(
                    [
                        self._price_formatter.round_price(it.count_total_value())
                        for it in invoice.invoice_items
                    ]
                ),
                invoice.currency,
            ),
            "total_invoice_tax": self._price_formatter.format_price(
                sum(
                    [
                        self._price_formatter.round_price(it.count_total_tax())
                        for it in invoice.invoice_items
                    ]
                ),
                invoice.currency,
            ),
            "total_invoice_without_tax": self._price_formatter.format_price(
                sum(
                    [
                        self._price_formatter.round_price(
                            it.count_total_value_without_tax()
                        )
                        for it in invoice.invoice_items
                    ]
                ),
                invoice.currency,
            ),
        }
