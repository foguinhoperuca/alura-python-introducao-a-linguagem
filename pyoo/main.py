from bank import Owner, Account
import logging
from util import Util


def test_transfer():
    nami_acc = Account(owner="Nami Straw Hat OO")
    nami_acc.deposit(99.00)
    print(nami_acc.bank_statement())
    marco_acc = Account(owner="Marco Phoenix Whitebeard OO")
    marco_acc.deposit(200.00)
    print(marco_acc.bank_statement())

    print("----------")

    marco_acc.transfer(10.00, nami_acc)
    print(nami_acc.bank_statement())
    print(marco_acc.bank_statement())

    # print(f"Marco balance - PRIVATE ATTRIBUTE: ${marco_acc._Account__balance}")


def test_owner():
    luffy = Owner("Luffy Strawhat Mugiwara", 20)
    print(f"{luffy.name} :: {luffy.age}")
    luffy.age = 25
    print(f"{luffy.name} :: {luffy.age}")


logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)
print("+++++++++++")
shanks = Account(owner="Shanks Mugiwara")
shanks.deposit(100.00)
print(shanks.bank_statement())

# print(f"{ shanks.can_withdrawn(200.00)=}")
print(f"{ shanks._Account__can_withdrawn(200.00)=}")

try:

    money = shanks.withdrawn(1050.00)
    print(f"Money withdrawn was ${money}")
except Exception as err:
    print("I am sorry!! You can't withdrawn.")
    print(f"Error message: {err}")
print("***********")
