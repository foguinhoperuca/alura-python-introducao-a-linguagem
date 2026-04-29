from typing import List, Set, Tuple

from termcolor import colored


CGATTRS: List[str] = ['bold', ]
STOP_KEYWORDS: Tuple[str] = ('exit', 'bye', 'end', 'quit', 'salir', 'sair', 'adios')


def exerc_01() -> None:
    """
    Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
    Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.
    Exemplo de entrada:
    > Digite o nome do convidado: Ana
    > Digite o nome do convidado: João
    > Digite o nome do convidado: Ana
    > Digite o nome do convidado: Carla
    > Digite o nome do convidado: sair
    Saída esperada: Convidados confirmados: Ana, João, Carla
    """
    print(f'{colored("[SETS_DICTS][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    guests: Set = set()
    while True:
        guest: str = input("Inform the guest's name: ")
        if guest.lower() in STOP_KEYWORDS:
            print(f'{colored("[SETS_DICTS][01]", "white", attrs=CGATTRS)} guests: {colored(guests, "red", attrs=CGATTRS)}')
            break

        guests.add(guest)


def exerc_02() -> None:
    """
    Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
    Exemplo de entrada:
    > Texto 1: O sol brilha forte no céu azul
    > Texto 2: O céu azul anuncia um dia de sol intenso
    Saída esperada: Palavras em comum: {'o', 'azul', 'sol', 'céu'}
    """
    texts: List[str] = [
        'O sol brilha forte no céu azul',
        'O céu azul anuncia um dia de sol intenso'
    ]
    print(f'{colored("[SETS_DICTS][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    text_01: Set = set(texts[0].lower().split(' '))
    text_02: Set = set(texts[1].lower().split(' '))
    print(f'{colored("[SETS_DICTS][02]", "white", attrs=CGATTRS)} {colored(text_01.intersection(text_02), "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
    - Quais itens apareceram nas duas listas
    - Quais foram exclusivos de Laura
    - Quais foram exclusivos da Ana
    Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
    Exemplo de entrada:
    > Lista de Laura: leite, pão, café, açúcar
    > Lista de Ana: pão, café, biscoito, chocolate
    Saída esperada:
    > Itens em ambas as listas: pão, café
    > Itens exclusivos de Laura: leite, açúcar
    > Itens exclusivos de Ana: biscoito, chocolate
    """
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    shopping_list_01: Set = set(['leite', 'pão', 'café', 'açúcar'])
    shopping_list_02: Set = set(['pão', 'café', 'biscoito', 'chocolate'])
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} shopping list 01............: {colored(shopping_list_01, "red", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} shopping list 02............: {colored(shopping_list_02, "yellow", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items in all lists..........: {colored(shopping_list_01.intersection(shopping_list_02), "magenta", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items exclusive in list 01..: {colored(shopping_list_01.difference(shopping_list_02), "blue", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items exclusive in list 02..: {colored(shopping_list_02.difference(shopping_list_01), "cyan", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    TODO start it
    """
    print(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_05() -> None:
    """
    TODO start it
    """
    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_06() -> None:
    """
    TODO start it
    """
    print(f'{colored("[SETS_DICTS][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][06]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_07() -> None:
    print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_08() -> None:
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_09() -> None:
    print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_10() -> None:
    print(f'{colored("[SETS_DICTS][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[SETS_DICTS][10]", "white", attrs=CGATTRS)} TODO implement!!')
