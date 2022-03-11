from __future__ import annotations

from dataclasses import dataclass
from typing import List, Any, Dict

import arrow
from arrow import Arrow

from invoice_generator.domain.invoice_item import InvoiceItem


@dataclass
class Invoice:
    document_number: str
    date_of_issue: Arrow
    sale_date: Arrow
    seller: List[str]
    buyer: List[str]
    invoice_items: List[InvoiceItem]
    logo_url: str
    account_number: str
    days_for_pay: int
    currency: str

    @classmethod
    def from_dict(cls, input_data: Dict[str, Any]) -> Invoice:
        return cls(
            document_number=input_data['document_number'],
            date_of_issue=arrow.get(input_data['date_of_issue']),
            sale_date=arrow.get(input_data['sale_date']),
            seller=input_data['seller'].splitlines(),
            buyer=input_data['buyer'].splitlines(),
            invoice_items=[InvoiceItem.from_dict(it) for it in input_data['invoice_items']],
            logo_url=input_data['logo_url'],
            account_number=input_data['account_number'],
            currency=input_data['currency'],
            days_for_pay=input_data['days_for_pay']
        )
