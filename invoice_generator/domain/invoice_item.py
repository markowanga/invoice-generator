from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class InvoiceItem:
    name: str
    unit: str
    amount: float
    net_single_price: float
    tax: float

    @classmethod
    def from_dict(cls, input_dict: Dict[str, Any]) -> InvoiceItem:
        return cls(
            name=input_dict['name'],
            unit=input_dict['unit'],
            amount=input_dict['amount'],
            net_single_price=input_dict['net_single_price'],
            tax=input_dict['tax']
        )

    def count_total_tax(self) -> float:
        return self.amount * self.net_single_price * self.tax

    def count_total_value(self) -> float:
        return self.count_total_value_without_tax() + self.count_total_tax()

    def count_total_value_without_tax(self) -> float:
        return self.amount * self.net_single_price
