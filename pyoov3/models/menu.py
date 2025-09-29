from abc import ABC, abstractmethod
from enum import auto, StrEnum
from typing import override, Self


class Item(ABC):
    def __init__(self: Self, name: str, value: float) -> None:
        self._name: str = name
        self._value: float = value

    def __str__(self: Self) -> str:
        return f'{self._name} ${self._value}'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def value(self: Self) -> str:
        return self._value

    @abstractmethod
    def discount(self) -> float:
        ...


class Bevarage(Item):
    DISCOUNT_RATE: float = 0.05

    class Size(StrEnum):
        SMALL = auto()
        MEDIUM = auto()
        BIG = auto()

    def __init__(self: Self, name: str, value: float, size: Size) -> None:
        super().__init__(name=name, value=value)
        self._size: Bevarage.Size = size

    def __str__(self: Self) -> str:
        return super().__str__() + f' :: size: {self._size}'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def size(self: Self) -> Size:
        return self._size

    @override
    def discount(self) -> float:
        return round((self._value * Bevarage.DISCOUNT_RATE), 2)


class Dish(Item):
    DISCOUNT_RATE: float = 0.08

    def __init__(self: Self, name: str, value: float, description: str) -> None:
        super().__init__(name=name, value=value)
        self._description: str = description

    def __str__(self: Self) -> str:
        return super().__str__() + f' :: description: {self._description}'

    @property
    def description(self: Self) -> str:
        return self._description

    @override
    def discount(self) -> float:
        return round((self._value * Dish.DISCOUNT_RATE), 2)


class Desert(Item):
    DISCOUNT_RATE: float = 0.15

    def __init__(self: Self, name: str, value: float, is_sweet: bool) -> None:
        super().__init__(name=name, value=value)
        self._is_sweet: bool = is_sweet

    def __str__(self: Self) -> str:
        return super().__str__() + f' :: is_sweet: {self._is_sweet}'

    @property
    def is_sweet(self: Self) -> bool:
        return self._is_sweet

    @override
    def discount(self) -> float:
        return round((self._value * Dish.DISCOUNT_RATE), 2)
