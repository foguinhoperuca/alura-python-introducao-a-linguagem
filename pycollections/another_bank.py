from functools import total_ordering

@total_ordering
class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __str__(self):
        return f">>code: {self._code} and balance: ${self._balance}<<"

    def __repr__(self):
        return f"REPR: ||code: {self._code} and balance: ${self._balance}||"

    def __eq__(self, other):
        eq = False
        # if type(other) == SalaryAccount:
        if isinstance(other, SalaryAccount):
            eq = self._code == other.code

        return eq

    def __lt__(self, other):
        if self._balance == other.balance:
            return self._code < other.code
        else:
            return self._balance < other.balance

    @property
    def code(self):
        return self._code

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        self._balance += value



class MultipleSalaries(SalaryAccount):
    pass