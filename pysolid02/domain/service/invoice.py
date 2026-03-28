from decimal import Decimal
import logging
from typing import Dict, Protocol, List, Self

from domain.entities import Order, ShippingType
from domain.service.shipping import EconomyShippingStrategy, ExpressShippingStrategy, NormalShippingStrategy
from util import DEFAULT_LOGGER_NAME


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

        self.__logger = logging.getLogger(DEFAULT_LOGGER_NAME)
        # self.__logger.setLevel = logging.DEBUG
        # self.__logger.setFormatter(logging.Formatter(Util.LOG_FORMAT_DEBUG))

    def generate_document(self: Self) -> str:
        return f'Invoice for {self._order.client}: ${self.calculate_total():.2f} with taxes already included.'

    def calculate_total(self: Self) -> Decimal:
        base_value: Decimal = self._order.calculate_total()

        # TODO implement shipping before tax
        shipping_value: Decimal = round(Decimal('0.00'), 2)
        if self._order.shipping_type is ShippingType.NORMAL:
            shipping_value = NormalShippingStrategy().calculate_shipping(order=self._order)
        elif self._order.shipping_type is ShippingType.EXPRESS:
            shipping_value = ExpressShippingStrategy().calculate_shipping(order=self._order)
        elif self._order.shipping_type is ShippingType.ECONOMY:
            shipping_value = EconomyShippingStrategy().calculate_shipping(order=self._order)

        selling_price: Decimal = base_value + shipping_value
        tax_values: Dict = {}
        for tax in self._taxes:
            tax_values[tax] = tax.calculate(base=selling_price)

        total_taxes: Decimal = sum(value for index, value in tax_values.items())
        total: Decimal = selling_price + total_taxes

        self.__logger.info(f'*** SOME LOGGING {DEFAULT_LOGGER_NAME} ***')
        print('')
        print('----- CALCULATION MEMORY -----')
        print(f'base value......: ${base_value:.2f}')
        print(f'shipping value..: ${shipping_value:.2f}')
        print(f'selling price...: ${selling_price:.2f}')
        print(f'total taxes.....: ${total_taxes:.2f} {[f"{index} = ${value}" for index, value in tax_values.items()]}')
        print(f'total...........: ${total:.2f}')
        print('----- CALCULATION MEMORY -----')
        print('')

        return total
