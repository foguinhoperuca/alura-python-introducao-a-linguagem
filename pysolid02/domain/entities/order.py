from decimal import Decimal
from enum import auto, Enum
from typing import List, Self

from domain.entities.product import Product
from domain.entities.client import Client


# FIXME should create a new module shipping?!
class ShippingType(Enum):
    NORMAL = auto()
    EXPRESS = auto()
    ECONOMY = auto()


class Order:
    def __init__(self: Self, client: Client, shipping_type: ShippingType = ShippingType.NORMAL) -> None:
        self._client: Client = client
        self._itens: List[Product] = []
        self._shipping_type: ShippingType = shipping_type

    @property
    def client(self: Self) -> Client:
        return self._client

    @property
    def itens(self: Self) -> List[Product]:
        return self._itens

    @property
    def shipping_type(self: Self) -> ShippingType:
        return self._shipping_type

    def add(self: Self, product: Product) -> None:
        self._itens.append(product)

    def calculate_total(self: Self) -> Decimal:
        return sum(product.price for product in self._itens)
