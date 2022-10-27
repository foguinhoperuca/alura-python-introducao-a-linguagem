from print_dict import pd
from util import account_factory, deposit, withdraw, balance

procedural_acc = account_factory(123, "Nico Robin Procedural", 55.0, 1000.0)
print(f"Your procedural account is:")
pd(procedural_acc)
deposit(procedural_acc, 45.0)
withdraw(procedural_acc, 10.00)
balance(procedural_acc)
print(f"Your FINAL procedural account is:")
pd(procedural_acc)
print("*****************************************************")
