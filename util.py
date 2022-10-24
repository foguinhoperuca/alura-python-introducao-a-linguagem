import logging
from termcolor import colored, cprint

class Util:
    """Helper class used to provide configuration, defaults and so on."""
    LOG_FORMAT_FULL = colored('[%(asctime)s][%(process)d:%(processName)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_DEBUG = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
    LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'

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