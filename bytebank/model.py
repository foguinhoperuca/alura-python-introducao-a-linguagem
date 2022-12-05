from datetime import date
from decimal import Decimal


class Employee:
    def __init__(self, name: str, birthday: str, wage: Decimal):
        self._name = name
        self._birthday = birthday
        self._wage = round(Decimal(wage), 2)
        self._partners = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']

    def __str__(self):
        return f"Employee: name>:{self._name} birthday>:{self._birthday} wage>: ${self._wage}"

    @property
    def name(self):
        return self._name

    @property
    def birthday(self):
        return self._birthday

    @property
    def wage(self):
        return self._wage

    @property
    def partners(self):
        return self._partners

    def age(self):
        return date.today().year - int(self.birthday.split('-')[0])

    def given_name(self):
        return self._name.strip().split(' ')[-1]

    def _is_partner(self):
        return self._wage >= 100000.00 and self.given_name() in self._partners

    def reduce_salary(self):
        if self._is_partner():
            self._wage *= round(Decimal(0.9), 2)

    def bonus(self):
        # return round(Decimal(0.00), 2) if self._wage * Decimal(0.1) > Decimal(1000.00) else round(Decimal(self._wage * Decimal(0.1)), 2)

        if self._wage * round(Decimal(0.10), 2) > round(Decimal(1000.00), 2):
            raise Exception(f'No bonus is allowed to {self._name} - wage is ${self._wage}')
        else:
            due_bonus = self._wage * round(Decimal(0.1), 2)

        return due_bonus
