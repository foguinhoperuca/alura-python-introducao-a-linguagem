from datetime import datetime
from functools import wraps
import logging

from termcolor import colored

LOG_FORMAT_INFO = colored('[%(filename)s#%(funcName)s:%(lineno)d]', 'white', attrs=['bold', 'dark']) + colored('[%(levelname)s]', 'magenta', attrs=['bold', 'dark']) + ' %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT_INFO)


"""See more examples at https://realpython.com/primer-on-python-decorators/ - https://github.com/realpython/materials/tree/master/primer-on-python-decorators"""


def not_during_the_night(func):
    def wrapper():
        # if 7 <= datetime.now().hour < 22:
        if 7 <= datetime.now().hour < 13:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def communication(func):
    def talk(s: str = "shiiiiiuuuuu"):
        print("----------------------------")
        print(f"talking: {func(s)}")
        print("============================")

    return talk


def information_exchange(func):
    @wraps(func)
    def propagate(*args, **kwargs):
        print("----------------------------")
        print(f"propagating: {func(*args, **kwargs)}")
        print("============================")

    return propagate


@communication
def shoult_out(say: str = "aaaa!!") -> str:
    return f"shout out: {say.upper()}"


@information_exchange
def whisper(say: str = "PÇPÇPÇPÇPÇ") -> str:
    return f"whisping: {say.lower()}"


@information_exchange
def normal_talk(*args, **kwargs):
    for arg in args:
        logging.debug(f"{arg=}")

    for key, value in kwargs.items():
        logging.debug(f"{key=} :: {value=}")

    return f"normal talk: {arg[0]}"


@not_during_the_night
def say_whee():
    print("Whee!")


shoult_out("Jeff")
print("..........")
whisper("lalalala")
print("..........")
whisper()
print("..........")
whisper(say='A')

normal_talk('Hello', 'World', a=1, b=2)
print("::::::::::")
say_whee()

# say = not_during_the_night(say_whee)
# say()
