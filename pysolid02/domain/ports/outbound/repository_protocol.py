from abc import ABC, abstractmethod
from typing import Generic, List, Self, TypeVar

from domain.entities import Cart


T = TypeVar('T')


class GetRepository(ABC, Generic[T]):
    @abstractmethod
    def read(self: Self, item_id: str) -> T:
        ...


class GetAllRepository(ABC, Generic[T]):
    @abstractmethod
    def read_all(self: Self) -> List[T]:
        ...


class InsertRepository(ABC, Generic[T]):
    @abstractmethod
    def save(self: Self, data: T) -> None:
        ...


class DeleteRepository(ABC, Generic[T]):
    @abstractmethod
    def remove(self: Self, item_id: str) -> None:
        ...


class UpdateRepository(ABC, Generic[T]):
    @abstractmethod
    def update(self: Self, data: T, item_id: str) -> None:
        ...


class CartRepositoryProtocol(ABC, GetRepository[Cart], GetAllRepository[Cart], InsertRepository[Cart], DeleteRepository[Cart], UpdateRepository[Cart]):
    ...
