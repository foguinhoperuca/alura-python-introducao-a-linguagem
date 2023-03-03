from termcolor import colored

LOG_FORMAT_INFO = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'

PRIORITY_QUEUE_TAG = 'PR'
NORMAL_QUEUE_TAG = 'NM'

DEFAULT_MAX_LENGTH = 300
DEFAULT_MIN_LENGTH = 0
