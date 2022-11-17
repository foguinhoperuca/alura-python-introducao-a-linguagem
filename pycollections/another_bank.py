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

    @property
    def code(self):
        return self._code

    def deposit(self, value):
        self._balance += value


class MultipleSalaries(SalaryAccount):
    pass