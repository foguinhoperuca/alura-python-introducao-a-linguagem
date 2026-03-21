from decimal import Decimal
from typing import List, Self

from domain.entities.product import Product
from domain.entities.client import Client


class Order:
    def __init__(self: Self, client: Client) -> None:
        self._client: Client = client
        self._itens: List[Product] = []

    @property
    def client(self: Self) -> Client:
        return self._client

    @property
    def itens(self: Self) -> List[Product]:
        return self._itens

    def add(self: Self, product: Product) -> None:
        self._itens.append(product)

    def calculate_total(self: Self) -> Decimal:
        return sum(product.price for product in self._itens)
