from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
import logging
from typing import Self, List

from client import Client
from item import Item


class Order(ABC):
    def __init__(self: Self, client: Client, itens: List[Item]) -> None:
        self._client: Client = client
        self._itens: List[Item] = itens

    def __str__(self: Self) -> str:
        return f"Receipt for {self._client} -> {self.quantity()} iten(s) with total: ${self.total()} -> {[item for item in self._itens]}"

    def __repr__(self: Self) -> str:
        return self.__str__()

    @abstractmethod
    def total(self: Self) -> Decimal:
        ...

    def quantity(self: Self) -> int:
        return len(self._itens)


class Delivery(Order):
    MINIMUM_DELIVERY_FEE: Decimal = Decimal(5.00)

    def __init__(self: Self, client, itens: List[Item], delivery_fee: Decimal = Decimal(5.00)) -> None:
        super().__init__(client=client, itens=itens)
        self._delivery_fee: Decimal = delivery_fee
        if delivery_fee < Delivery.MINIMUM_DELIVERY_FEE:
            logging.warning(f'Delivery fee must be ${Delivery.MINIMUM_DELIVERY_FEE:.2f} or higher. ${delivery_fee:.2f} will be not accepted!')
            self._delivery_fee = Delivery.MINIMUM_DELIVERY_FEE

    def __str__(self: Self) -> str:
        return super().__str__().replace(' -> ', f' -> delivery fee: ${self._delivery_fee}; ')

    def total(self: Self) -> Decimal:
        return Decimal(sum(item.price for item in self._itens)) + self._delivery_fee


class Takeout(Order):
    def total(self: Self) -> Decimal:
        return Decimal(sum(item.price for item in self._itens))


class Gift(Order):
    class GiftCardType(Enum):
        NORMAL = Decimal('4.99')
        URGENT = Decimal('9.99')

    def __init__(self: Self, client: Client, itens: List[Item], gift_card: GiftCardType = GiftCardType.NORMAL) -> None:
        super().__init__(client=client, itens=itens)
        self._gift_card: Gift.GiftCardType = gift_card

    def __str__(self: Self) -> str:
        return super().__str__().replace(' -> ', f' -> gift card: ${round(self._gift_card.value, 2)} ({self._gift_card.name}); ')

    def total(self: Self) -> Decimal:
        return round(Decimal(sum(item.price for item in self._itens)) + self._gift_card.value, 2)


class Special(Order):
    HANDLING_FEE: Decimal = Decimal('0.10')

    def __str__(self: Self) -> str:
        return super().__str__().replace(' -> ', f' -> original total plus {Special.HANDLING_FEE * 100}% as handling fee; ')

    def total(self: Self) -> Decimal:
        return round(Decimal(sum(item.price for item in self._itens)) * Decimal(1 + Special.HANDLING_FEE), 2)
