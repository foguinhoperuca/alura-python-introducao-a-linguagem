from decimal import Decimal
from enum import auto, StrEnum
from typing import Self


class ProductType(StrEnum):
    DIGITAL: str = auto()
    PHYSICAL: str = auto()


class Product:
    def __init__(self: Self, sku: str, name: str, price: Decimal, quantity: int, prod_type: ProductType) -> None:
        self._sku: str = sku
        self._name: str = name
        self._price: Decimal = round(price, 2)
        self._quantity: int = quantity
        self._prod_type: ProductType = prod_type

    def __str__(self: Self) -> str:
        return f'[{self._sku}] ({self._quantity}) {self._name} ${self._price}'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def sku(self: Self) -> int:
        return self._sku

    @property
    def price(self: Self) -> Decimal:
        return self._price

    def is_available(self: Self) -> bool:
        return True if self._quantity > 0 else False
