from decimal import Decimal
import pytest
from pytest import mark

from bytebank.model import Employee


class TestClass:
    @pytest.fixture
    def employee(self):
        return Employee(name="José Carlos Silva e Santos", birthday="2001-01-31", wage=Decimal(7211.00))

    @pytest.fixture
    def tester(self):
        return Employee(name="Tester00 PM Sorocaba", birthday='2000-03-13', wage=Decimal(1111.00))

    @pytest.fixture
    def no_bonus_employee(self):
        return Employee(name="No donuts for you!", birthday="2001-04-01", wage=Decimal(37541.82))

    # def test_parse_string(self, employee):
    #     assert str(employee) == "Employee: name>:José Carlos Silva e Santos birthday>:2001-01-31 wage>: $7211.00"

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self, tester):
        print("")
        print("------------------------- XPTO -------------------------")

        expected_result = 22
        res = tester.age()
        assert res == expected_result

        tester00 = Employee(name="Tester", birthday="2000-04-01", wage=1111.00)
        print(f"Tester age: {tester00.age()}")
        assert tester00.age() == 22

        tester01 = Employee(name="Tester", birthday="1999-03-13", wage=2222.00)
        print(f"Tester age: {tester01.age()}")
        assert tester01.age() == 23

        tester02 = Employee(name="Tester", birthday="1998-05-01", wage=3333.00)
        print(f"Tester age: {tester02.age()}")
        assert tester02.age() == 24
        print("------------------------- XPTO -------------------------")

    @mark.employee_name
    def test_grab_given_name(self, employee):
        # tester_given_name = Employee(name="José Carlos Silva e Santos", birthday="2001-00-31", wage=7211.00)
        # res = tester_given_name.given_name()
        # print("")
        # print("------------------------- XPTO -------------------------")
        # print(tester_given_name)
        # print(tester_given_name.given_name())
        # print("------------------------- XPTO -------------------------")
        res = employee.given_name()
        assert res == "Santos"

        assert employee.name == "José Carlos Silva e Santos"

    @mark.employee_name
    def test_employee_partner(self):
        original_wage = Decimal(100000.00)
        partner_name = "Paulo Bragança"
        reduced_salary = round(Decimal(90000.00), 2)

        partner = Employee(partner_name, "1980-04-01", original_wage)
        partner.reduce_salary()
        result = partner.wage

        assert result == reduced_salary

        assert partner.given_name() in partner.partners

    # @mark.skip
    @mark.calc_bonus
    def test_employee_bonus(self, employee, tester):
        expected_bonus_employee = round(Decimal(721.10), 2)
        realized_bonus_employee = employee.bonus()
        assert expected_bonus_employee == realized_bonus_employee

        expected_bonus_tester = round(Decimal(111.10), 2)
        realized_bonus_tester = tester.bonus()
        assert expected_bonus_tester == realized_bonus_tester

    # @mark.skip
    @mark.calc_bonus
    def test_employee_bonus_not_due(self, no_bonus_employee):
        with pytest.raises(Exception):
            expected_bonus_no_bonus_employee = 0.00
            realized_bonus_no_bonus_employee = no_bonus_employee.bonus()
            assert expected_bonus_no_bonus_employee == realized_bonus_no_bonus_employee
