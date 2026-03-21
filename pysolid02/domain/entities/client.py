from typing import Self
from uuid import uuid4


class Client:
    def __init__(self: Self, name: str, email: str) -> None:
        self._id: uuid4 = uuid4()
        self._name: str = name
        self._email: str = email

    def __str__(self: Self) -> str:
        return f'[{self._id}] {self._name} ({self._email})'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def id(self: Self) -> uuid4:
        return self._id

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def email(self: Self) -> str:
        return self._email
