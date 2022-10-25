from random import randrange

class Account:
    def __init__(self, owner, number=randrange(0, 1000), limit=1000.00):
        self._owner = owner
        self._number = number
        self._limit = limit
        self._balance = 0.00
        print(f"Account created at memory address {self}")

    def deposit(self, value):
        self._balance += value

    def withdrawn(self, value):
        self._balance -= value

    def transfer(self, value):
        self.withdrawn(value)

        return value

    def say_balance(self):
        print(f"You balance, **{self._owner}** acc #{self._number}, is ${self._balance}. You still have the follow limit: ${self._limit}.")