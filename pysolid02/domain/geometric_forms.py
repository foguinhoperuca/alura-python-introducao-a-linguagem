from abc import ABC, abstractmethod
from typing import Self


class Forms(ABC):
    @abstractmethod
    def area(self: Self) -> float:
        ...


class Rectangule(Forms):
    def __init__(self: Self, width: float, height: float) -> None:
        self._width: float = width
        self._height: float = height

    def area(self: Self) -> float:
        return self._width * self._height


class Square(Forms):
    def __init__(self: Self, width: float) -> None:
        self._width: float = width

    def area(self: Self) -> float:
        return self._width * self._width


class Triangule(Forms):
    def __init__(self: Self, base: float, height: float) -> None:
        self._base: float = base
        self._height: float = height

    def area(self: Self) -> float:
        return (self._base * self._height) / 2
