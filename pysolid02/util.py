import logging

from termcolor import colored


LOG_FORMAT_FULL = colored('[%(asctime)s][%(process)d:%(processName)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s '
LOG_FORMAT_INFO = colored('[%(asctime)s]', 'green', attrs=['bold', 'dark']) + colored('[%(filename)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
DEFAULT_LOGGER_NAME = 'pysolid02'
DATETIME_FORMAT = "%Y-%m-%dT%H-%M-%S"


def init_logger(log_type='normal'):
    if log_type == 'quiet':
        level = logging.WARN
        logformat = LOG_FORMAT_SIMPLE
    elif log_type == 'verbose':
        level = logging.DEBUG
        logformat = LOG_FORMAT_FULL
    else:                   # elif log_type == 'normal':
        level = logging.INFO
        logformat = LOG_FORMAT_INFO

    app_logger = logging.getLogger(DEFAULT_LOGGER_NAME)
    app_logger.setLevel(level)

    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter(logformat))
    c_handler.setLevel(level)
    app_logger.addHandler(c_handler)

    return app_logger
