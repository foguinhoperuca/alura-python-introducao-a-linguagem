from typing import List, Self
from uuid import UUID

from domain.entities import Cart
from domain.ports.outbound import CartRepositoryProtocol


LIST_CART: List[Cart] = []


class CartRepository(CartRepositoryProtocol):
    def __init__(self: Self, list_cart: List[Cart]) -> None:
        self._list_cart: List[Cart] = list_cart

    def read(self: Self, item_id: UUID) -> Cart:
        return [unique for unique in self._carts if unique.cart_id == item_id][0]

    def read_all(self: Self) -> List[Cart]:
        return self._list_cart

    def save(self: Self, data: Cart) -> None:
        assert data is Cart

        self._list_cart.append(data)

    def remove(self: Self, item_id: UUID) -> None:
        cart: Cart = [unique for unique in self._carts if unique.cart_id == item_id][0]
        self._list_cart.remove(cart)

    def update(self: Self, data: Cart, item_id: UUID) -> None:
        self.remove(item_id=item_id)
        self.save(data=data)
