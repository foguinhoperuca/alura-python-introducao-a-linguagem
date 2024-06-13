import matplotlib
from math import pow
import numpy as np
from random import choice, randrange
from typing import List


def challenge_03() -> None:
    rnd_list: List[int] = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
    print(f'Choice is: {choice(rnd_list)}')


def challenge_04() -> None:
    print(f'{randrange(100)=}')


def challenge_05() -> None:
    number_01: int = int(input('Inform number 01: '))
    number_02: int = int(input('Inform number 02: '))

    print(f'{pow(number_01, number_02)=}')


def challenge_06() -> None:
    pass


def challenge_07() -> None:
    pass


def challenge_08() -> None:
    pass


def challenge_09() -> None:
    pass


def challenge_10() -> None:
    pass
