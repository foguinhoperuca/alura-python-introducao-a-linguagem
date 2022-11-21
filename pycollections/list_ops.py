from operator import attrgetter
from decimal import Decimal
from tuples_examples import CheckingAccount, SavingAccount, InvestmentAccount
import array as arr
import numpy as np
from another_bank import SalaryAccount, MultipleSalaries

def extract_balance(acc: SalaryAccount) -> Decimal:
    return acc.balance


def next_age(age: int):
    return age + 1


def deposit_for_all(accs):
    for acc in accs:
        acc.deposit(100.00)


def do_visual_process(ages=None):
  # print(len(ages))
  if ages == None:
      ages = list()

  print(f"{len(ages)=:02} ::: {ages=}")
  ages.append(13)


def first_class():
    ages = [10, 25, 39, 47, 58, 63, 72, 81, 93]
    for age in ages:
        print(f"{age}")

    print("")
    print(f"{ages[5]=} ::: {type(ages)=}")

    print(f"{len(ages)=:02} ::: {ages=}")

    ages.append(39)
    ages.append(33)
    print(f"{len(ages)=:02} ::: {ages=}")
    # print(f"{ages[25]}")
    ages.remove(39)
    print(f"{len(ages)=:02} ::: {ages=}")

    del_el = 99
    if del_el in ages:
        # nerver executed
        print(f"Removing {del_el} from {ages=}...")
        ages.remove(del_el)
        print(f"{len(ages)=:02} ::: {ages=}")

    del_el = 58
    if del_el in ages:
        print(f"Removing {del_el:02} from {ages=}...")
        ages.remove(del_el)
        print(f"{len(ages)=:02} ::: {ages=}")

    ages.clear()
    print(f"{len(ages)=:02} ::: {ages=}")
    print("-----------------")

    ages.insert(0, 69)
    ages.insert(1, 80)
    ages.insert(2, 71)
    ages.insert(3, 52)
    print(f"{len(ages)=:02} ::: {ages=}")
    ages.insert(1, 19)
    print(f"{len(ages)=:02} ::: {ages=}")

    more_ages = [26, 18]
    ages.insert(len(ages), more_ages)
    print(f"{len(ages)=:02} ::: {ages=}")
    ages.remove(more_ages)
    print(f"{len(ages)=:02} ::: {ages=}")
    ages.extend(more_ages)
    print(f"{len(ages)=:02} ::: {ages=}")

    aged = []
    for age in ages:
        aged.append(age + 1)

    print(f"{len(aged)=:02} ::: {aged=}")
    agef = [age + 1 for age in ages]
    print(f"{len(agef)=:02} ::: {agef=}")
    print(f"{len(ages)=:02} ::: {ages=}")

    ageg = [age for age in ages if age > 21]
    print(f"{len(ages)=:02} ::: {ages=}")
    print(f"{len(ageg)=:02} ::: {ageg=}")

    ageh = [next_age(age) for age in ages]
    print(f"{len(ages)=:02} ::: {ages=}")
    print(f"{len(ageh)=:02} ::: {ageh=}")

    print("**********")
    # do_visual_process(ages)
    do_visual_process()
    # print(f"{len(ages)=:02} ::: {ages=}")
    do_visual_process()
    do_visual_process()
    do_visual_process()

def second_class():
    gui = CheckingAccount(1)
    dani = CheckingAccount(2)
    accounts = [gui, dani]
    for account in accounts:
        print(account)
    print("******")
    print(f"{gui}")
    gui.deposit(500.00)
    print(f"{gui}")
    print(f"{dani}")
    dani.deposit(999.99)
    print(f"{dani}")
    gui.deposit(100.00)
    print(f"{gui}")
    print("********************")
    more_accounts = [gui, dani, gui]
    more_accounts[2].deposit(200)
    for account in more_accounts:
        print(account)
    # print(gui)
    deposit_for_all(accounts)
    print("###############")
    for account in accounts:
        print(account)
    print("@@@@@@@@@@@@")
    accounts.insert(0, 76)
    for account in accounts:
        print(account)
    # deposit_for_all(accounts) # not works!!! int in list with other objects
    guilherme = ('Guilherme', 37, 1981)
    daniela = ('Daniela', 31, 1987)
    print(guilherme)
    print(daniela)
    users = [guilherme, daniela]
    print(f"{users=}")
    users.append(('Paulo', 37, 1979))
    print(f"{users=}")
    print("++++++++++++++")
    gui_acc = CheckingAccount(15)
    gui_acc.deposit(501)
    dani_acc = CheckingAccount(234587)
    dani_acc.deposit(1399.00)
    accs_tuple = (gui_acc, dani_acc)
    for acc in accs_tuple:
        print(f"{acc=}")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    gui_acc.deposit(33.54)
    for acc in accs_tuple:
        print(f"{acc=}")

def third_class():
    account16 = CheckingAccount(16)
    account16.deposit(1000)
    print(account16)
    account16.next_month()
    print(account16)
    account17 = SavingAccount(17)
    account17.deposit(1000)
    print(account17)
    account17.next_month()
    print(account17)
    accounts = [account16, account17]
    for account in accounts:
        account.next_month()
    a = arr.array('d', [1, 3.5])
    print(a)
    try:
        a2 = arr.array('d', [1, 3.5, 'Jeff'])
    except Exception as e:
        print(e)
    narr = np.array([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    for n in narr:
        print(f"{n:02} * 2 = {(n * 2):02}")
    try:
        account18 = InvestmentAccount(18)
        account.next_month()
    except Exception as e:
        print(e)


def until_class_04():
    gui_payment = SalaryAccount(38)
    gui_payment.deposit(19)
    gui_again = SalaryAccount(38)
    gui_again.deposit(19)
    paulo_payment = SalaryAccount(40)
    paulo_payment.deposit(20)
    payments = [gui_payment]
    ch_acc = CheckingAccount(38)
    multiple_salaries = MultipleSalaries(38)
    print(f"gui_payment == gui_again? {gui_payment == gui_again}")
    print(f"gui_payment == paulo_payment? {gui_payment == paulo_payment}")
    print(f"gui_payment in payments? {gui_payment in payments}")
    print(f"gui_again in payments? {gui_again in payments}")
    print(f"paulo_payment in payments? {paulo_payment in payments}")
    print(f"gui_payment == ch_acc? {gui_payment == ch_acc}")
    print(f"gui_payment == multiple_salaries? {gui_payment == multiple_salaries}")

def until_class_06():
    ages = [15, 87, 32, 65, 56, 32, 49, 37]
    i = 0
    for age in ages:
        print(f"{i = } {age = }")
        i += 1
    print('----------------------------')
    for i in range(0, len(ages)):
        print(f"{i = } age: {ages[i]}")
    print('----------------------------')
    for i, age in enumerate(ages):
        print(f"{i = } age: {age}")
    print('----------------------------')
    lst = list(enumerate(ages))
    print(f"{lst = }")
    for item in lst:
        print(f"{item[0]:02} -- {item[1]:03}")
    print('----------------------------')
    users = [
        ("Guilherme", 37, 1981),
        ("Daniela", 31, 1987),
        ("Paulo", 39, 1979)
    ]
    for name, _, _ in users:
        # print(name, birthday, age)
        print(name, _, _)
    print('----------------------------')
    gen = list(range(len(ages)))
    print(gen)
    # print(lst)
    print('----------------------------')
    ssss = sorted(ages)
    srsr = sorted(ages, reverse=True)
    rrrr = list(reversed(ages))
    lrsa = list(reversed(sorted(ages)))
    print(f"{ages = }")
    print(f"{ssss = }")
    print(f"{srsr = }")
    print(f"{rrrr = }")
    print(f"{lrsa = }")
    ages.sort()
    print(f"{ages = }")

def final_class_course_01():
    gui_acc = SalaryAccount(17)
    gui_acc.deposit(500)
    dani_acc = SalaryAccount(3)
    dani_acc.deposit(1000)
    paulo_acc = SalaryAccount(133)
    paulo_acc.deposit(510)
    joao_acc = SalaryAccount(15)
    joao_acc.deposit(500)
    julio_acc = SalaryAccount(169)
    julio_acc.deposit(1700)
    accounts = [gui_acc, dani_acc, paulo_acc, joao_acc, julio_acc]
    for account in accounts:
        print(account)
    print(f"{sorted(accounts, key=extract_balance) = }")
    # print(f"{a = }")
    print("************************************************")
    print(f"{(gui_acc < dani_acc) = }")
    print(f"{(gui_acc > dani_acc) = }")
    print(f"{sorted(accounts) = }")
    for a in sorted(accounts, reverse=True):
        print(a)
    print(sorted(accounts))
    print(f"{(gui_acc <= joao_acc) = }")
    print(f"{(gui_acc == gui_acc) = }")


