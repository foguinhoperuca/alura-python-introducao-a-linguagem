import list_ops
from tuples_examples import CheckingAccount, SavingAccount, InvestmentAccount
import array as arr
import numpy as np
from another_bank import SalaryAccount, MultipleSalaries


if __name__ == "__main__":
    print("")
    print("*******************************************")
    print("|| Python Collection 01: List and Tuples ||")
    print("*******************************************")
    print("")

    # list_ops.first_class()
    # print("/////////////////////////////////////////////////////")
    # print("")
    #
    # list_ops.second_class()
    # print("/////////////////////////////////////////////////////")
    # print("")
    #
    # list_ops.third_class()
    # print("/////////////////////////////////////////////////////")
    # print("")

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