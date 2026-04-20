from decimal import Decimal
from enum import StrEnum, auto
from typing import List, Optional, Self
from uuid import UUID, uuid4

from domain.entities.product import Product


class CartStatus(StrEnum):
    ACTIVE = auto()
    FINISHED = auto()
    EXPIRED = auto()


class Cart:
    def __init__(self: Self, products: List[Product], cart_id: Optional[UUID] = None) -> None:
        self._products: List[Product] = products
        self._cart_id: Optional[UUID] = cart_id
        self._status: CartStatus = CartStatus.ACTIVE
        self._subtotal: Decimal = round(Decimal('0.00'), 2)

    @property
    def cart_id(self: Self) -> UUID:
        if self._cart_id is None:
            self._cart_id = uuid4()

        return self._cart_id

    def add(self: Self, product: Product) -> None:
        self._products.append(product)

    def remove(self: Self, product: Product) -> None:
        self._products.remove(product)

    def _calculate_subtotal(self: Self) -> Decimal:
        prices: List[Decimal] = [product.price() for product in self._products if product.is_available()]
        total: Decimal = sum(prices)  # type: ignore
        self._subtotal = total

        return total

    @property
    def subtotal(self: Self) -> Decimal:
        self._calculate_subtotal()

        return self._subtotal

    @property
    def status(self: Self) -> CartStatus:
        return self._status

    def switch(self: Self, new_status: CartStatus) -> CartStatus:
        self._status = new_status

        return self._status
