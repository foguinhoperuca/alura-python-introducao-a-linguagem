from enum import StrEnum, auto
from typing import List, Optional, Self
from uuid import uuid4

from domain.entities.product import Product


class CartStatus(StrEnum):
    ACTIVE: str = auto()
    FINISHED: str = auto()
    EXPIRED: str = auto()


class Cart:
    def __init__(self: Self, products: List[Product], cart_id: Optional[uuid4] = None) -> None:
        self._products: List[Product] = products
        self._cart_id: uuid4 = cart_id
        self._status: CartStatus = CartStatus.ACTIVE
