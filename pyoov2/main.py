import logging

from bank import Account
from  util import Util


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
    print('pyoo v2')
    logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)

    number: int = 123
    owner: str = 'Nico'
    balance: float = 55.00
    limit: float = 1000.0

    account: Account = create_account()
    acc_by_dict: Account = create_account_by_dict()

    print(f'--- Account......: {account}')
    print(f'--- acc by dict..: {acc_by_dict}')

    print(account.bank_statement())
