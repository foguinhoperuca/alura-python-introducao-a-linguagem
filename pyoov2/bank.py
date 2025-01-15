from datetime import datetime
import logging
from typing import Self


class Account:
    def __init__(self, number: int, owner: str, balance: float, limit: float) -> None:
        self.__logger = logging.getLogger('PYOOV2')
        self.__logger.setLevel = logging.DEBUG
        # self.__logger.setFormatter(logging.Formatter(Util.LOG_FORMAT_DEBUG))

        self.__number: int = number
        self.__owner: str = owner
        self.__balance: float = balance
        self.__limit: float = limit

    def __str__(self) -> str:
        return f'[{self.__number}] owner: {self.__owner} has ${self.__balance} with limit of ${self.__limit}'

    @property
    def owner(self) -> str:
        return self.__owner

    def deposit(self, value: float) -> None:
        self.__balance += value

    def withdrawn(self, value: float) -> float:
        self.__balance -= value

        return value

    def bank_statement(self) -> str:
        statement: str = f"Your balance, **{self.__owner}** acc #{self.__number}, is ${self.__balance}. You still have the follow limit: ${self.__limit}."
        self.__logger.debug(statement)

        return statement

    def transfer(self, destiny: Self, ammount: float) -> None:
        money: float = self.withdrawn(ammount)
        destiny.deposit(money)

        self.__logger.info(f'Transfered ${ammount} FROM {self.owner} TO {destiny.owner} AT {datetime.now()}')
