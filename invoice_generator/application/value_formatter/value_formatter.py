from abc import ABC, abstractmethod

from arrow import Arrow


class ValueFormatter(ABC):

    @abstractmethod
    def round_price(self, value: float) -> float:
        pass

    @abstractmethod
    def format_date(self, date: Arrow) -> str:
        pass

    @abstractmethod
    def format_price(self, price_value: float, currency: str) -> str:
        pass

    @abstractmethod
    def format_value(self, value: float) -> str:
        pass
