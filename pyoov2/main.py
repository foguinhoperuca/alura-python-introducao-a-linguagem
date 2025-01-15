import logging
import sys

from bank import Account
from exercises import CustomData, Rectangule
sys.path.append('.')
from util import Util


def create_account() -> Account:
    return Account(number=number, owner=owner, balance=balance, limit=limit)


def create_account_by_dict() -> Account:
    acc_dict: dict = {
        'number': 321,
        'owner': 'Gohan',
        'balance': 473.22,
        'limit': 2500.00
    }

    return Account(number=acc_dict['number'], owner=acc_dict['owner'], balance=acc_dict['balance'], limit=acc_dict['limit'])


if __name__ == "__main__":
    bot_logger = logging.getLogger('PYOOV2')
    bot_logger.setLevel(logging.INFO)
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter(Util.LOG_FORMAT_SIMPLE))
    c_handler.setLevel(logging.INFO)
    bot_logger.addHandler(c_handler)
    # logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)
    # logging.basicConfig(level=logging.INFO, format=colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s')  # noqa: E501

    custom_data: CustomData = CustomData(day='20', month='01', year='2025')
    bot_logger.info(f'formated data: {custom_data.formated()}')
    r = Rectangule(7, 6)
    r._Rectangule__area = 7  # mangling ;)
    print(r.get_area())
    print('--------------------------------------------------')

    number: int = 123
    owner: str = 'Nico'
    balance: float = 55.00
    limit: float = 1000.0
    account: Account = create_account()
    acc_by_dict: Account = create_account_by_dict()
    print(f'--- Account......: {account}')
    print(f'--- acc by dict..: {acc_by_dict}')

    print('Initial bank statement:')
    print(f'=== {account.bank_statement()}')

    account.deposit(value=10.00)
    print('After deposit $10.00')
    print(f'=== {account.bank_statement()}')

    account.withdrawn(value=7.50)
    print('After withdrawn 7.50')
    print(f'=== {account.bank_statement()}')

    print('\n')
    print('--- ACCOUNT TRANSFER ---')
    print('\n')
    account02: Account = Account(number=9, owner='Robin', balance=350.00, limit=3000.00)
    print('account02 bank statement:')
    print(f'::: {account02.bank_statement()}')
    account02.transfer(ammount=50.00, destiny=account)
    print('After all:')
    print(f'::: {account.bank_statement()}')
    print(f'::: {account02.bank_statement()}')

    print('--- Finished Program')
