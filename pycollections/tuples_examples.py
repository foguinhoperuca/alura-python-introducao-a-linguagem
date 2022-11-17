from abc import ABCMeta, abstractmethod
from decimal import Decimal


class Account(metaclass=ABCMeta):
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __str__(self):
        return f">>code: {self._code} and balance: ${self._balance}<<"

    def __repr__(self):
        return f"REPR: ||code: {self._code} and balance: ${self._balance}||"

    def deposit(self, value: Decimal):
        self._balance += value

    @abstractmethod
    def next_month(self):
        pass


class CheckingAccount(Account):
    def next_month(self):
        self._balance -= 2


class SavingAccount(Account):
    def next_month(self):
        self._balance *= 1.01
        self._balance -= 3


class InvestmentAccount(Account):
    pass