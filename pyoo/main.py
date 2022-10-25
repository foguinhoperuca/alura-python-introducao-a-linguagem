from print_dict import pd
from util import account_factory, deposit, withdraw, balance
from account import Account

procedural_acc = account_factory(123, "Nico Robin Procedural", 55.0, 1000.0)
print(f"Your procedural account is:")
pd(procedural_acc)
deposit(procedural_acc, 45.0)
withdraw(procedural_acc, 10.00)
balance(procedural_acc)
print(f"Your FINAL procedural account is:")
pd(procedural_acc)
print("*****************************************************")

nami_acc = Account(owner="Nami Straw Hat OO")
nami_acc.deposit(99.00)
nami_acc.say_balance()

print("----------")

marco_acc = Account(owner="Marco Phoenix Whitebeard OO")
marco_acc.deposit(200.00)
marco_acc.say_balance()

print("+++++++++++")

print(f"Marco balance: ${marco_acc._balance}")
