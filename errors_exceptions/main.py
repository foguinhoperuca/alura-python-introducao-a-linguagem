import traceback
import sys

from byte_bank import Client, CheckingAccount, InsufficiencyBalanceError, FinancialOperationError
from reader import ByteBankReader


if __name__ == "__main__":
    try:
        a = 10
        b = 2
        c = a / b
        print(f'First division is: {c}')
        b = 0
        c = a / b
        print(f'Second division is: {c}')
    except ZeroDivisionError as ex:
        print('Zero division error! Errro is:')
        sep1 = '=' * len(str(ex))
        sep2 = '-' * len(str(ex))
        print('===' + sep1 + '===')
        print('|| ' + sep2 + ' ||')
        print(f'|| {ex} ||')
        print('|| ' + sep2 + ' ||')
        print('===' + sep1 + '===')

    john = Client(name='Jhon Doe', document='12345678-90', profession='Software Engineer')
    luigi = Client(name='Luigi Doe', document='09876543-21', profession='Designer')
    checking_account = CheckingAccount(client=john, agency='0001', number=12345, balance=256.512)
    john_acc = CheckingAccount(client=john, agency='0001', number=12345, balance=256.512)
    luigi_acc = CheckingAccount(client=luigi, agency='0001', number=54321, balance=512.32)

    try:
        print("")
        print("---XX")
        checking_account_error = CheckingAccount(client=john, agency='0001', number='12345', balance=256.512)
        print(f"Balance is: {checking_account_error.bank_statement()}")
    except Exception as ex:
        print('Got some error')
        print(f'EXCEPTION: {ex} ; ARG: {ex.args[1]}')

    try:
        print("")
        print("---")
        checking_account.withdrawn(200.00)
        print(f'Actual balance is: {checking_account.bank_statement()}')
        checking_account.withdrawn(300.00)
        print(f'Actual balance is: {checking_account.bank_statement()}')
    except (InsufficiencyBalanceError, FinancialOperationError) as ex:
        print('No more money in checking account!!')
        print(ex)

    try:
        luigi_acc.transfer(16.08, john_acc)
        print("")
        print("---")
        print(f'Bank statement of {john.name} is ${john_acc.bank_statement()}')
        print(f'Bank statement of {luigi.name} is ${luigi_acc.bank_statement()}')
        luigi_acc.transfer(1024.16, john_acc)
        print(f'Bank statement of {john.name} is ${john_acc.bank_statement()}')
        print(f'Bank statement of {luigi.name} is ${luigi_acc.bank_statement()}')
    except FinancialOperationError as ex:
        print("Using raise from here!!!!")
        print(ex)
        print("......................................................")
        print(f"CAUSE: {ex.__cause__}")
        traceback.print_exc()
        print("......................................................")

    try:
        balance = 64.08
        withdrawn = 256.16
        raise InsufficiencyBalanceError(f'Insufficienty balance: ${balance} in account. Tried to remove ${withdrawn}', balance, withdrawn, 'SOME CUSTOM PROPERTY TO RAISE EXCEPTION')
    except (InsufficiencyBalanceError, FinancialOperationError) as ex:
        print("")
        print("NO MORE MONEY!! Custom message")
        print(ex)
        print("...")

    # max_accounts = 1000000
    # accounts = []
    # while (True):
    #     try:
    #         accounts.append(CheckingAccount(client=john_acc, agency='0001', number=(len(accounts) + 1), balance=256.512))
    #         if len(accounts) > max_accounts:
    #             raise Exception("Reached the max number of accounts!!", max_accounts)
    #     except KeyboardInterrupt:
    #         print("")
    #         print(f'Total of accounts is: {len(accounts)}')
    #         sys.exit(1)
    #     except Exception as ex:
    #         print("")
    #         print(f"Got error: {ex}")
    #         break

    try:
        with ByteBankReader('file_test.txt') as reader:
            reader.read_next_line()
    except Exception() as ex:
        print(ex)

    sys.exit(0)
