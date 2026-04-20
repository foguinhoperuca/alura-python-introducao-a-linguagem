from typing import List, Self
from uuid import UUID

from domain.entities import Cart, CartStatus
from domain.ports.outbound import CartRepositoryProtocol, NotifyByEmail, NotifyByPhone
from domain.value_object import Email, Phone


class SwitchCartUseCase:
    def __init__(self: Self, repository: CartRepositoryProtocol, notify_emails: List[NotifyByEmail], notify_cellphones: List[NotifyByPhone]) -> None:
        self._repository: CartRepositoryProtocol = repository
        self._notify_emails: List[NotifyByEmail] = notify_emails
        self._notify_cellphones: List[NotifyByPhone] = notify_cellphones

    def execute(self: Self, cart_id: UUID, new_status: CartStatus, email: Email, cellphone: Phone) -> Cart:
        cart_entity: Cart = self._repository.read(item_id=cart_id)
        cart_entity.switch(new_status)
        message: str = f'Cart change status to: {new_status.value}'
        for notify_email in self._notify_emails:
            notify_email.send_message(message, email)

        for notify_cellphones in self._notify_cellphones:
            notify_cellphones.send_message(message, cellphone)

        return cart_entity
