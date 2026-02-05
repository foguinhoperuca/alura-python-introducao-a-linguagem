from abc import ABC, abstractmethod
from decimal import Decimal
from enum import auto, Enum
import logging
from typing import List, Self

from client import Client
from item import Item
from notification import NotificationFacade


class OrderStatus(Enum):
    CREATED: int = auto()
    CONFIRMED: int = auto()
    ON_PREPARE: int = auto()
    ON_ROUTE: int = auto()
    DELIVERED: int = auto()


class Order(ABC):
    def __init__(self: Self, client: Client, itens: List[Item]) -> None:
        self._client: Client = client
        self._itens: List[Item] = itens
        self._status: OrderStatus = OrderStatus.CREATED
        self._observers: List[ObserverOrderStatus] = []

    def __str__(self: Self) -> str:
        return f"Receipt for {self._client} -> {self.quantity()} iten(s) with total: ${self.total()} -> {[item for item in self._itens]}"

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def client(self: Self) -> Client:
        return self._client

    @property
    def itens(self: Self) -> List[Item]:
        return self._itens

    @property
    def status(self: Self) -> OrderStatus:
        return self._status

    @status.setter
    def status(self: Self, vl: OrderStatus) -> None:
        if vl is OrderStatus.CONFIRMED:
            logging.info(f'Order for {self._client} is CONFIRMED!!')

        self._status = vl
        self.notify()

    # FIXME should be a @property?
    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def notify(self: Self) -> None:
        for observer in self._observers:
            observer.update(self)

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


class ObserverOrderStatus:
    def __init__(self: Self, notification: NotificationFacade) -> None:
        self._notification: NotificationFacade = notification

    def update(self: Self, order: Order) -> None:
        self._notification.send(client=order.client, message=f'[{order.status.name}] Your order with {len(order.itens)} is ready to go!')
