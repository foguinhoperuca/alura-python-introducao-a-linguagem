from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Self

from domain.entities import Order


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self: Self, order: Order) -> Decimal:
        ...


class NormalShippingStrategy(ShippingStrategy):
    def calculate_shipping(self: Self, order: Order) -> Decimal:
        return round(Decimal('10.00'), 2)


class ExpressShippingStrategy(ShippingStrategy):
    def calculate_shipping(self: Self, order: Order) -> Decimal:
        return round(Decimal('20.00'), 2)


class EconomyShippingStrategy(ShippingStrategy):
    def calculate_shipping(self: Self, order: Order) -> Decimal:
        return round(Decimal('5.00'), 2)
