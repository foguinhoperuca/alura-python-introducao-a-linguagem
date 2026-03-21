from decimal import Decimal
from typing import Dict, Protocol, List, Self

from domain.entities import Order


class TaxStrategy(Protocol):
    def calculate(self: Self, base: Decimal) -> Decimal:
        ...


class ISS(TaxStrategy):
    ALIQUOT: Decimal = round(Decimal('0.02'), 2)

    def __init__(self: Self, aliquot: Decimal = ALIQUOT) -> None:
        self._name: str = 'Imposto Sobre Serviço'
        self._aliquot: Decimal = aliquot

    def __str__(self: Self) -> str:
        return f'{self._name} ({round((Decimal(self._aliquot) * 100), 2)}%)'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def aliquot(self: Self) -> Decimal:
        return self._aliquot

    def calculate(self: Self, base: Decimal) -> Decimal:
        return round((base * self._aliquot), 2)


class ICMS(TaxStrategy):
    ALIQUOT: Decimal = round(Decimal('0.10'), 2)

    def __init__(self: Self, aliquot: Decimal = ALIQUOT) -> None:
        self._name: str = 'Imposto Sobre Circulação de Mercadoria'
        self._aliquot: Decimal = aliquot

    def __str__(self: Self) -> str:
        return f'{self._name} ({round((Decimal(self._aliquot) * 100), 2)}%)'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def aliquot(self: Self) -> Decimal:
        return self._aliquot

    def calculate(self: Self, base: Decimal) -> Decimal:
        return round((base * self._aliquot), 2)


class IVA(TaxStrategy):
    ALIQUOT: Decimal = round(Decimal('0.05'), 2)

    def __init__(self: Self, aliquot: Decimal = ALIQUOT) -> None:
        self._name: str = 'Imposto Sobre Valor Agregado'
        self._aliquot: Decimal = aliquot

    def __str__(self: Self) -> str:
        return f'{self._name} ({round((Decimal(self._aliquot) * 100), 2)}%)'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def aliquot(self: Self) -> Decimal:
        return self._aliquot

    def calculate(self: Self, base: Decimal) -> Decimal:
        return round((base * self._aliquot), 2)


class InvoiceService:
    def __init__(self: Self, order: Order, taxes: List[TaxStrategy] = [ISS(), ICMS()]) -> None:
        assert order is not None
        assert len(taxes) >= 1
        self._order: Order = order
        self._taxes: List[TaxStrategy] = taxes

    def generate_document(self: Self) -> str:
        return f'Invoice for {self._order.client}: ${self.calculate_total():.2f} with taxes already included.'

    def calculate_total(self: Self) -> Decimal:
        base_value: Decimal = self._order.calculate_total()

        tax_values: Dict = {}
        for tax in self._taxes:
            tax_values[tax] = tax.calculate(base=base_value)

        total_taxes: Decimal = sum(value for index, value in tax_values.items())
        total: Decimal = base_value + total_taxes

        print('')
        print('----- CALCULATION MEMORY -----')
        print(f'base value...: ${base_value:.2f}')
        print(f'total taxes..: ${total_taxes:.2f} {[f"{index} = ${value}" for index, value in tax_values.items()]}')
        print(f'total........: ${total:.2f}')
        print('----- CALCULATION MEMORY -----')
        print('')

        return total
