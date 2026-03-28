from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Self


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self: Self, value: Decimal) -> Decimal:
        ...


class BirthdayDiscountStrategy(DiscountStrategy):
    def apply_discount(self: Self, value: Decimal) -> Decimal:
        return round(value * Decimal('0.50'), 2) if value >= round(Decimal('500.00'), 2) else value


class LoyaltyDiscountStrategy(DiscountStrategy):
    def apply_discount(self: Self, value: Decimal) -> Decimal:
        return round(value * Decimal('0.70'), 2) if value >= round(Decimal('300.00'), 2) else value


class ApplyDiscountStrategy:
    def __init__(self: Self, strategy: DiscountStrategy) -> None:
        self._strategy: DiscountStrategy = strategy

    def update(self: Self, new_strategy: DiscountStrategy) -> None:
        self._strategy = new_strategy

    def apply_discount(self: Self, value: Decimal) -> Decimal:
        assert value > round(Decimal('0.00'), 2)

        return self._strategy.apply_discount(value=value)
