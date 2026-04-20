from abc import ABC, abstractmethod
from typing import Self


class SimpleDriver(ABC):
    @abstractmethod
    def receive_ride(self: Self) -> None:
        ...


class AppDriver(ABC):
    @abstractmethod
    def shared_ride(self: Self) -> None:
        ...


class TransportDriver(ABC):
    @abstractmethod
    def transport_cargo(self: Self) -> None:
        ...


class TaxiDriver(SimpleDriver):
    def receive_ride(self: Self) -> None:
        print('RECEIVE RIDE...')


class Ubser(AppDriver):
    def shared_ride(self: Self) -> None:
        print('SHARED DRIVE...')


class Correios(TransportDriver):
    def transport_cargo(self: Self) -> None:
        print('TRANSPORT CARGO...')


if __name__ == '__main__':
    individual: SimpleDriver = SimpleDriver()
    uber: AppDriver = AppDriver()
    transport: TransportDriver = TransportDriver()

    
