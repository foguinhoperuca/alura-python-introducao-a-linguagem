from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


def exerc_01() -> None:
    """
    Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
    Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
    Exemplo de Entrada:
        Digite o item que você quer verificar: açúcar
    Saída esperada:
        O item açúcar precisa ser comprado.
    """
    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    pantry: List[str] = [
        'chocolate branco',
        'chocolate negro',
        'bolacha',
        'café',
        'leite',
        'arroz integral',
        'óleo de soja',
        'bandeija de ovos',
        'margarina sem sal',
    ]
    search: str = input(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} Inform a product to search: ')

    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} search in pantry? {colored(search in pantry, 'green', attrs=CGATTRS)}')

    for product in pantry:
        if search.lower() == product.lower():
            print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} product founded {colored(search, 'blue', attrs=CGATTRS)} ')
            return

    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} Product not found: {colored(search, 'red', attrs=CGATTRS)} - {colored('you need buy it!', 'yellow', attrs=CGATTRS)}')


def exerc_02() -> None:
    print(f'{colored("[LISTS_TUPLES][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_03() -> None:
    print(f'{colored("[LISTS_TUPLES][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_04() -> None:
    print(f'{colored("[LISTS_TUPLES][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_05() -> None:
    print(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_06() -> None:
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_07() -> None:
    print(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_08() -> None:
    print(f'{colored("[LISTS_TUPLES][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_09() -> None:
    print(f'{colored("[LISTS_TUPLES][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')


def exerc_10() -> None:
    print(f'{colored("[LISTS_TUPLES][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
