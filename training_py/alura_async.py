import asyncio
import time
from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


async def exerc_01() -> None:
    """
    TODO start it
    """
    async def coroutine(number: int) -> None:
        print(f'Running task {number}')
        await asyncio.sleep(number)
        print(f'Finished task {number}')

    async def coroutine_from_future(number: int, future: asyncio.Future) -> None:
        print(f'Start for number {number}')
        await asyncio.sleep(number)
        future.set_result(f'End for number {number}')

    print(f'{colored("[ALURA_ASYNC][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    # await asyncio.sleep(1)
    task_01 = asyncio.create_task(coroutine(number=1))
    task_02 = asyncio.create_task(coroutine(number=2))
    await task_01
    await task_02

    future_01 = asyncio.Future()
    asyncio.create_task(coroutine_from_future(number=1, future=future_01))
    result_01 = await future_01
    print(f'{result_01=}')

    print(f'{colored("[ALURA_ASYNC][01]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')
    time.sleep(1)


def exerc_02() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][04]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_05() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][05]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][06]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][07]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][08]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][09]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_10() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][10]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')
