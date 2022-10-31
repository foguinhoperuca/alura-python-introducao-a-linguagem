# from __future__ import annotations # FIXME set acc as Account object
# from typing import Self
import logging
from decimal import Decimal
from random import randrange
from util import Util


class Owner:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def say_hello(self):
        hello = f"Hello! My name is {self.__name}! I am {self.__age} years old."
        logging.debug(Util.warning(hello))

        return hello

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Account:
    @staticmethod
    def bank_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    BANK_CODE = bank_codes()['BB']
    # BANK_CODE = bank_codes.__func__()['BB']

    def __init__(self, owner: Owner, number=randrange(0, 1000, ), limit=1000.00):
        self.__owner = owner
        self.__number = number
        self.__max_limit = limit
        self.__limit = limit
        self.__balance = 0.00
        self.__transfer_rate = 8.0
        # self.__bank_code = "001"

    def deposit(self, value):
        self.__balance += value

    def __can_withdrawn(self, value: float) -> bool:
        logging.debug(f"{value=} :: {(self.__balance + self.__limit)=} :: {(value <= (self.__balance + self.__limit))=}")

        available_value = self.__balance + self.__limit
        return value <= available_value

    def withdrawn(self, value: float) -> float:
        if self.__can_withdrawn(value):
            self.__balance -= value
        else:
            raise Exception(f"Not allowed borrow this amount ${value}.")

        return value

    def withdrawn_with_loan(self, value):
        # TODO test it!
        if (self.__balance - value) < 0.00:  # value <= self.__balance
            logging.info("No funds! Grab money from limit to use!!")
            if ((self.__balance + self.__limit) - value) < 0.00:  # value <= self.__limit
                raise Exception("No funds or limit to withdrawn!!")
            else:
                logging.info("Using money from limit")
                borrowed_money = float(input(f"No funds! Would you like to loan some money? Your limit is"
                                             f" ${self.__limit} (if yes inform value > 0.00): "))
                if ((self.__balance + self.__limit) - borrowed_money) < 0.00:
                    raise Exception(f"Not allowed borrow this amount ${borrowed_money}.")

                # FIXME consdider balance and limit to decrease
                self.__limit -= borrowed_money
                money = borrowed_money
        else:
            self.__balance -= value
            money = value

        return money

    def transfer(self, value, destiny_account: 'Account') -> Decimal:
        original_balance = self.__balance
        money = (self.withdrawn(value + self.__transfer_rate) - self.__transfer_rate)
        rate_paid = self.__transfer_rate
        destiny_account.deposit(money)

        logging.info(
            f"Asked ${value} to be transferred. In fact, was transferred ${money} (paid {rate_paid})"
            f" to account #{destiny_account.number} owner {destiny_account.owner.name}. "
            f"Now, {self.__owner.name}, you still have ${self.__balance} of original "
            f"balance ${original_balance} in account #{self.__number} with limit ${self.__limit}."
        )

        # print("**********************")
        # print(randrange(0, 1000))
        # print(f"{destiny_account.number} == {self.__number}? {destiny_account.number == self.__number}")

        return value

    def bank_statement(self):
        statement = f"Your balance, **{self.__owner.name}** acc #{self.__number}, is ${self.__balance}. You still have " \
                    f"the follow limit: ${self.__limit}. "
        logging.info(statement)

        return statement

    @property
    def owner(self):
        return self.__owner

    @property
    def number(self):
        return self.__number

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @property
    def max_limit(self):
        return self.__max_limit

    @max_limit.setter
    def max_limit(self, max_limit):
        self.__max_limit = max_limit

    @property
    def balance(self):
        return self.__balance

    @property
    def transfer_rate(self):
        return self.__transfer_rate

    @transfer_rate.setter
    def transfer_rate(self, transfer_rate):
        self.__transfer_rate = transfer_rate
