import logging
from termcolor import colored, cprint


def account_factory(number, owner, balance, limit):
    return {
        "number": number,
        "owner": owner,
        "balance": balance,
        "limit": limit
    }


def deposit(account, value):
    orig_balance = account['balance']
    account["balance"] += value
    print(f"You original balance is ${orig_balance}. You will deposit ${value}. The final balance is ${account['balance']}")


def withdraw(account, value):
    orig_balance = account['balance']
    account["balance"] -= value
    print(f"You original balance is ${orig_balance}. You will withdrawn ${value}. The final balance is ${account['balance']}")


def balance(account):
    print(f"The account's balance is ${account['balance']}")


class Util:
    """Helper class used to provide configuration, defaults and so on."""
    LOG_FORMAT_FULL = colored('[%(asctime)s][%(process)d:%(processName)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_DEBUG = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    GEO_02_NEW_OUTPUT: str = 'geo/data/geo02_new/output'
    GEO_02_NEW_INPUT: str = 'geo/data/geo02_new/input'
    GEO_02_NEW_DATA: str = 'alura_curso_geopandas_02/dados'

    # # FIXME Why I need instantiate Util class?!?! Make all methods statics wouldn't be enough?!?
    # def __init__(self):

    def info(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'cyan')

    def warning(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'yellow', attrs=['bold'])

    def error(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'red', attrs=['bold', 'underline'])

    def debug(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'green', attrs=['reverse', 'bold', 'underline'])

    def critical(msg):
        """This function standardize the message and simplified the use to standard output."""
        return colored(msg, 'red', attrs=['bold', 'underline', 'blink'])
