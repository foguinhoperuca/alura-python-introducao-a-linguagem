from typing import Self


class Client:
    def __init__(self, name: str, address: str) -> None:
        self._name: str = name
        self._address: str = address

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def address(self: Self) -> str:
        return self._address

