from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


def class02() -> None:
    print(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} custom code')
    phrase: str = input(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} inform a phrase:\n')
    words: List[str] = phrase.split(' ')
    print(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} total words: {len(words)}')


def exerc_01() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    value: float = float(input(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} inform the value: $'))
    tip_percentage: float = float(input(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} inform tip percentage: %'))
    tip: float = value * (tip_percentage / 100)
    total: float = value + tip
    print(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} value {colored(f"${value:.2f}", "red", attrs=CGATTRS)} tip percentage {colored(f"{tip_percentage:.2f} %", "magenta", attrs=CGATTRS)} total tip {colored(f"${tip:.2f}", "yellow", attrs=CGATTRS)} final value: {colored(f"${total:.2f}", "cyan", attrs=CGATTRS)}')


def exerc_02() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][03]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][04]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_05() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_10() -> None:
    """
    TODO start it
    """
    print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')
