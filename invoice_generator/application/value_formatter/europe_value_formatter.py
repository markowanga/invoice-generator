from arrow import Arrow

from invoice_generator.application.value_formatter.value_formatter import ValueFormatter


class EuropeValueFormatter(ValueFormatter):

    def round_price(self, value: float) -> float:
        return round(value, 2)

    def format_date(self, date: Arrow) -> str:
        return date.format('DD.MM.YYYY')

    def format_value(self, value: float) -> str:
        return '{:,.2f}'.format(value).replace(',', ' ').replace('.', ',')

    def format_price(self, price_value: float, currency: str) -> str:
        value_str = '{:,.2f}'.format(self.round_price(price_value)).replace(',', ' ').replace('.',
                                                                                              ',')
        return f'{value_str} {currency}'
