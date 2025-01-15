class CustomData:
    def __init__(self, day: str, month: str, year: str) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        return f'{self._day}/{self._month}/{self._year}'

    def __repr__(self) -> str:
        return self.__str__()

    def formated(self) -> str:
        return self.__str__()


class Rectangule:
    def __init__(self, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y
        self.__area: float = x * y

    def get_area(self) -> float:
        return self.__area
