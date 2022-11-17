from tuples_examples import CheckingAccount, SavingAccount, InvestmentAccount
import array as arr
import numpy as np


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
