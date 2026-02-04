from abc import ABC, abstractmethod
from enum import auto, Enum
import logging
from typing import Dict, List, Self

from client import Client


class NotificationStatus(Enum):
    SUCCESS = auto()
    ERROR = auto()


class Notification(ABC):
    @abstractmethod
    def send(self: Self, client: Client, message: str) -> NotificationStatus:
        ...


class NotificationEmail(Notification):
    MESSAGE_SIZE: int = 1024

    def send(self: Self, client: Client, message: str) -> NotificationStatus:
        status: NotificationStatus = NotificationStatus.ERROR
        if len(message) <= NotificationEmail.MESSAGE_SIZE:
            status = NotificationStatus.SUCCESS
            print(f'[EMAIL] Sending message for {client}: {message}')
            return status

        logging.error(f'Invalid message size: Notification lenght should be less than {NotificationEmail.MESSAGE_SIZE} (found {len(message)})')

        return status


class NotificationSMS(Notification):
    MESSAGE_SIZE: int = 128

    def send(self: Self, client: Client, message: str) -> NotificationStatus:
        status: NotificationStatus = NotificationStatus.ERROR
        if len(message) <= NotificationSMS.MESSAGE_SIZE:
            status = NotificationStatus.SUCCESS
            print(f'[SMS] Sending message for {client}: {message}')
            return status

        logging.error(f'Invalid message size: Notification lenght should be less than {NotificationEmail.MESSAGE_SIZE} (found {len(message)})')

        return status


class NotificationFacade:
    def __init__(self: Self) -> None:
        self._notifications: List[Notification] = [
            NotificationEmail(),
            NotificationSMS()
        ]

    def send(self, client: Client, message: str) -> None:
        statuses: Dict[Notification, NotificationStatus] = dict()
        error: bool = False

        for notification in self._notifications:
            statuses[notification] = notification.send(client, message)
            if statuses[notification] is NotificationStatus.ERROR:
                error = True

        if error:
            logging.error(f'Got some error sending notification for client {client} :: message: {message}')
