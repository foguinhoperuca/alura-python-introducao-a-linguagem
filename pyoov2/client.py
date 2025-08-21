from datetime import datetime
import logging


class Client:
    def __init__(self, name: str, birthday: datetime) -> None:
        self.__logger = logging.getLogger('PYOOV2')
        self.__name: str = name
        self.__birthday: datetime = birthday

    def __str__(self) -> str:
        return f'{self.__name} has born in {self.__birthday}'

    @property
    def logger(self) -> logging.Logger:
        return self.__logger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, vl: str) -> None:
        self.__name = vl

    @property
    def birthday(self) -> datetime:
        return self.__birthday

    @birthday.setter
    def birthday(self, vl: datetime) -> None:
        self.__birthday = vl
