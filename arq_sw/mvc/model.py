from typing import Self


class Attendant:
    def __init__(self: Self, name: str, sales: int = 0) -> None:
        assert self._valid_name(name) is True

        self._name: str = name
        self._sales: int = sales

    def __str__(self: Self) -> str:
        return f'Name: {self._name} :: sales: {self._sales}'

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def sales(self: Self) -> int:
        return self._sales

    def _valid_name(self: Self, name: str) -> bool:
        if not name:
            print('Name is empty. You must enter a name.')
            return False

        return True

    def increase_sales(self: Self, sales: int) -> None:
        self._sales += sales
