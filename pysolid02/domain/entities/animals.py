from abc import abstractmethod, ABC
from typing import Self


class Bird(ABC):
    @abstractmethod
    def type_of(self: Self) -> None:
        ...


class FlyBird(Bird):
    @abstractmethod
    def flight(self: Self) -> None:
        ...


class Canary(FlyBird):
    def type_of(self: Self) -> None:
        print('Type is Canary')

    def flight(self: Self) -> None:
        print('Flying as Canary')


class Penguim(Bird):
    def type_of(self: Self) -> None:
        print('Type is Penguim')


def show_flight(bird: Bird) -> None:
    if isinstance(bird, FlyBird):
        bird.flight()
    else:
        bird.type_of()


if __name__ == '__main__':
    tux: Bird = Penguim()
    show_flight(bird=tux)

    brazil: Bird = Canary()
    show_flight(bird=brazil)
