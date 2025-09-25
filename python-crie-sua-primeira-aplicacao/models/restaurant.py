from enum import StrEnum
from time import sleep
from typing import List, Optional, Self


class Categories(StrEnum):
    FAST_FOOD = 'Fast Food'
    ITALIAN = 'Italian Food'
    BRAZILIAN = 'Brazilian Food'
    FRENCH = 'French Food'
    JAPANESE = 'Japanese Food'
    CHINESE = 'Chinese Food'


class Client:
    def __init__(self: Self, name: str, years: int = 0) -> None:
        self._name: str = name
        self._years: int = years

    def __str__(self: Self) -> str:
        return f'Client {self._name} has {self._years} year(s) of loyalty'

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def years(self: Self) -> int:
        return self._years


class Review:
    def __init__(self, client: Client, grade: int = 1) -> None:
        self._grade: int = grade

    @property
    def grade(self: Self) -> int:
        return self._grade


class Restaurant:
    def __init__(self: Self, name: str, category: Categories = Categories.BRAZILIAN) -> None:
        self._name: str = name
        self._category: Categories = category
        self._state: bool = False
        self._reviews: List[Review] = []

    def __str__(self: Self) -> str:
        return f'Restaurant [{self._category.value}] {self._name} is {self._state} | Has {len(self._reviews)} reviews'

    def __repr__(self: Self) -> str:
        return self.__str__()

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def category(self: Self) -> Categories:
        return self._category

    @property
    def state(self: Self) -> bool:
        return self._state

    @property
    def reviews(self: Self) -> List[Review]:
        return self._reviews

    def is_active(self: Self) -> str:
        return '☑' if self._state else '☐'

    def toggle_state(self) -> None:
        self._state = not self._state


def restaurant_factory() -> Optional[Restaurant]:
    try:
        name: str = input('Inform the name of restaurant:\n')

        categories: List[str] = [e.value.upper() for e in Categories]
        while True:
            cat: str = input('Inform the category of restaurant:\n')

            if cat.upper() in categories:
                category: Categories = Categories(cat)
                break

            print(f'{cat} not found. Please inform one of follow:')
            for category in categories:
                print(f'- {category}')

            sleep(2)
            print('')

        return Restaurant(name=name, category=category)
    except Exception as e:
        print(f'Could not create music. Error: {e}')
        sleep(5)
        return None
