from bank import Owner, Account
import logging
from util import Util


def test_transfer():
    nami = Owner(name="Nami Straw Hat OO Owner", age=20)
    nami_acc = Account(owner=nami)
    nami_acc.deposit(99.00)
    print(nami_acc.bank_statement())

    marco = Owner(name="Marco Phoenix Whitebeard OO Owner", age=30)
    marco_acc = Account(owner=marco)
    marco_acc.deposit(200.00)
    print(marco_acc.bank_statement())

    print("----------")

    marco_acc.transfer(10.00, nami_acc)
    print(nami_acc.bank_statement())
    print(marco_acc.bank_statement())

    # print(f"Marco balance - PRIVATE ATTRIBUTE: ${marco_acc._Account__balance}")


def test_owner():
    luffy = Owner("Luffy Strawhat Mugiwara", 19)
    print(f"{luffy.name} :: {luffy.age}")
    luffy.age = 25
    print(f"Happy birthday {luffy.name} :: {luffy.age}")


logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)
print("+++++++++++")
shanks = Owner(name="Shanks Mugiwara OO Owner", age=35)
print(shanks.say_hello())
shanks_acc = Account(owner=shanks)
shanks_acc.deposit(100.00)
print(shanks_acc.bank_statement())
print(f"Bank code is: {Account.BANK_CODE}")
print(f"Available Bank codes is: Caixa: {Account.bank_codes()['Caixa']}; Bradesco: {Account.bank_codes()['Bradesco']};"
      f" BB: {Account.bank_codes()['BB']}")

# print(f"{ shanks.can_withdrawn(200.00)=}")
print(f"{ shanks_acc._Account__can_withdrawn(200.00)=}")

try:
    value = 1050.00
    money = shanks_acc.withdrawn(value)
    print(f"Money withdrawn was ${money}")
    value = 500.00
    more_money = shanks_acc.withdrawn(value)
    print(f"More money withdrawn was ${more_money}")
except Exception as err:
    print(f"I am sorry!! You can't withdrawn ${value}. {shanks_acc.bank_statement()}")
    print(f"Error message: {err}")
print("***********")
