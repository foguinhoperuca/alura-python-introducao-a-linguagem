from decimal import Decimal
from typing import Self


class Item:
    def __init__(self, name: str, price: Decimal) -> None:
        self._name: str = name
        self._price: Decimal = price

    def __str__(self: Self) -> str:
        return f'${self._price:.2f} - {self._name}'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def price(self: Self) -> Decimal:
        return self._price
