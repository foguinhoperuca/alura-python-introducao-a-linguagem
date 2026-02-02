from typing import Self


class Client:
    def __init__(self: Self, name: str, address: str) -> None:
        self._name: str = name
        self._address: str = address

    def __str__(self: Self) -> str:
        return f'{self._name} ({self._address})'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def address(self: Self) -> str:
        return self._address
