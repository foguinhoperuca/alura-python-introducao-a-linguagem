from __future__ import annotations
from typing_extensions import Self
from decimal import Decimal


class Client:
    def __init__(self, name: str, document: str, profession: str) -> None:
        self._name = name
        self._document = document
        self._profession = profession

    def __repr__(self):
        return f'NAME: {self._name} DOCUMENT: {self._document} PROFESSION: {self._profession}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def document(self) -> str:
        return self._document

    @document.setter
    def document(self, document: str) -> None:
        self._document = document

    @property
    def profession(self) -> str:
        return self._profession

    @profession.setter
    def profession(self, profession: str) -> None:
        self._profession = profession


class CheckingAccount:
    total_accounts: int = 0
    operation_rate: Decimal = 0.00

    def __init__(self, client: Client, agency: str, number: int, balance: Decimal = 100.00):
        self.__client = client
        self.__set_agency(agency)
        self.__set_number(number)
        self.__balance = balance
        self._not_allowed_withdrawn = 0
        self._not_allowed_transfer = 0
        CheckingAccount.total_accounts += 1
        CheckingAccount.operation_rate = 30 / CheckingAccount.total_accounts

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, value):
        if not isinstance(value, str):
            raise ValueError("This attr agency must be **str**!!", value)
        if int(value) <= 0:
            raise ValueError("This attr agency must be **>= 0**!!", value)

        self.__agency = value

    @property
    def number(self):
        return self.__number

    def __set_number(self, value):
        if not isinstance(value, int):
            raise ValueError("This attr account number must be **int**!!", value)
        if value <= 0:
            raise ValueError("This attr account number must be **>= 0**!!", value)

        self.__number = value

    def withdrawn(self, value: Decimal) -> Decimal:
        if value < 0:
            raise ValueError(f'The value {value} must be greater than 0!!')
        if value > self.__balance:
            self._not_allowed_withdrawn += 1
            raise InsufficiencyBalanceError(message='', balance=self.__balance, value=value)

        self.__balance -= value

        return value

    def deposit(self, value: Decimal) -> None:
        self.__balance += value

    def transfer(self, value: Decimal, destiny: Self) -> None:
        if value < 0:
            raise ValueError(f'The value {value} must be greater than 0!!')

        try:
            val = self.withdrawn(value)
        except InsufficiencyBalanceError as ex:
            self._not_allowed_transfer += 1
            ex.args = ()
            raise FinancialOperationError('Operation not finished!!') from ex

        destiny.deposit(val)

    def bank_statement(self) -> str:
        return self.__balance


class InsufficiencyBalanceError(Exception):
    def __init__(self, message='', balance=None, value=None, *args):
        self._balance = balance
        self._value = value
        msg = f'[GENERIC MESSAGE] Insufficient balance: ${self._balance} for withdrawn ${self._value}.'
        self._message = message or msg
        super(InsufficiencyBalanceError, self).__init__(self._message, self._balance, self._value, *args)


class FinancialOperationError(Exception):
    pass
