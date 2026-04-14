from abc import ABC, abstractmethod
from typing import Self

from domain.value_object import Email, Phone


class NotifyByPhone(ABC):
    @abstractmethod
    def send_message(self: Self, message: str, number: Phone) -> None:
        pass


class NotifyByEmail(ABC):
    @abstractmethod
    def send_message(self: Self, message: str, email: Email) -> None:
        pass
