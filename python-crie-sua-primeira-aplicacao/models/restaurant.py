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
    def __init__(self: Self, client_id: int, name: str, years: int = 0) -> None:
        self._client_id: int = client_id
        self._name: str = name
        self._years: int = years

    def __str__(self: Self) -> str:
        return f'Client {self._name} has {self._years} year(s) of loyalty'

    @property
    def client_id(self: Self) -> int:
        return self._client_id

    @property
    def name(self: Self) -> str:
        return self._name

    @property
    def years(self: Self) -> int:
        return self._years

    @classmethod
    def factory(cls: Self, client_id: int, name: str, years: int) -> Self:
        if client_id <= 0:
            raise ValueError(f'ID {id} is invalid!!')

        if name.strip() == '':
            raise ValueError(f'Name {name} is invalid!!')

        if years < 0:
            raise ValueError(f'Years {years} is invalid!!')

        return Client(client_id=client_id, name=name, years=years)


class Review:
    MAX_RATING: int = 5
    MIN_RATING: int = 1

    def __init__(self, client: Client, rating: int = 1) -> None:
        self._client: Client = client
        self._rating: int = rating

    @property
    def client(self: Self) -> Client:
        return self._client

    @property
    def rating(self: Self) -> int:
        return self._rating

    @classmethod
    def validate(cls: Self, client: Client, rating: int) -> bool:
        is_valid: bool = True

        # TODO validate client

        if not isinstance(rating, int):
            raise ValueError(f'Invalid rating: {rating}. Only integer values from range {Review.MIN_RATING} (inclusive) to {Review.MAX_RATING} (inclusive)')

        if rating < cls.MIN_RATING or rating > cls.MAX_RATING:
            is_valid = False

        return is_valid


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

    @reviews.setter
    def reviews(self: Self, vl: Review) -> None:
        if Review.validate(vl):
            self._reviews.append(vl)

        raise ValueError(f'Value {vl} is invalid. No review is added')

    @classmethod
    def get_category_from_str(cls: Self, cat: str) -> Optional[Categories]:
        categories: List[str] = [e.value.upper() for e in Categories]

        return Categories(cat) if cat.upper() in categories else None

    def is_active(self: Self) -> str:
        return '☑' if self._state else '☐'

    def toggle_state(self) -> None:
        self._state = not self._state

    def avarage_rating(self: Self) -> float:
        """
        Return avarage rating from all reviews.
        When no review was made return 0.
        See reviews to know the range.
        """
        if not self._reviews:
            return 0.0

        return round(sum(review._rating for review in self._reviews) / len(self._reviews), 2)

    @classmethod
    def factory(cls: Self, name_factory: Optional[str] = None, category_factory: Optional[str] = None) -> Optional[Self]:
        try:
            name: str = input('Inform the name of restaurant:\n') if name_factory is None else name_factory

            categories: List[str] = [e.value.upper() for e in Categories]
            while True:
                cat: str = input('Inform the category of restaurant:\n') if category_factory is None else category_factory

                if cat.upper() in categories:
                    category: Categories = Categories(cat)
                    break

                print(f'{cat} not found. Please inform one of follow:')
                for register in categories:
                    print(f'- {register}')

                sleep(2)
                print('')

            return Restaurant(name=name, category=category)
        except Exception as e:
            print(f'Could not create music. Error: {e}')
            sleep(5)
            return None
