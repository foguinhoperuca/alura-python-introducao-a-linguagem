import logging


class Account:
    def __init__(self, number: int, owner: str, balance: float, limit: float) -> None:
        self.__number: int = number
        self.__owner: str = owner
        self.__balance: float = balance
        self.__limit: float = limit

    def __str__(self) -> str:
        return f'[{self.__number}] owner: {self.__owner} has ${self.__balance} with limit of ${self.__limit}'

    def deposit(self, value: float) -> None:
        self.__balance += value

    def withdrawn(self, value: float) -> float:
        self.__balance -= value

        return value

    def bank_statement(self) -> str:
        statement: str = f"Your balance, **{self.__owner}** acc #{self.__number}, is ${self.__balance}. You still have the follow limit: ${self.__limit}."
        logging.info(statement)

        return statement
