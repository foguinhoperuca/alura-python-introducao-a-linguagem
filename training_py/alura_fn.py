from typing import List, Tuple
from datetime import datetime

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


def exerc_01() -> None:
    """
    Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.
    Exemplo de entrada:
    > Digite o ano de nascimento: 2005
    > Digite o ano atual: 2025
    Saída esperada: A idade é 20 anos.
    """
    def age(year_birthday: int) -> int:
        return datetime.now().year - year_birthday

    print(f'{colored("[FN][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    year: int = int(input(f"{colored("[FN][01]", "white", attrs=CGATTRS)} Inform your birthday's year: "))
    print(f'{colored("[FN][01]", "white", attrs=CGATTRS)} your estimated age: {colored(age(year), "red", attrs=CGATTRS)}')


def exerc_02() -> None:
    """
    Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
    Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
    Exemplo de entrada: Digite uma palavra: tecnologia
    Saída esperada: Essa palavra tem 10 caracteres.
    """
    def count_chars(w: str) -> int:
        return len(w)

    print(f'{colored("[FN][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    word: str = input(f'{colored("[FN][02]", "white", attrs=CGATTRS)} Inform a word: ')
    print(f'{colored("[FN][02]", "white", attrs=CGATTRS)} size of word: {colored(count_chars(word), "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
    Se for antes das 12h, exibir "Bom dia";
    Entre 12h e 18h, exibir "Boa tarde";
    Após 18h, exibir "Boa noite".
    Exemplo de entrada: Digite a hora atual (0-23): 15
    Saída esperada: Boa tarde!
    """
    def greet(hr: int) -> str:
        match hr:
            case h if 0 <= h < 12:
                return 'Good moorning!'
            case h if 12 <= h <= 18:
                return 'Good afternoon!'
            case h if 18 < h <= 24:
                return 'Good night!'
            case _:
                return f'Invalid hour: {h}'

    print(f'{colored("[FN][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    hour: int = int(input(f'{colored("[FN][03]", "white", attrs=CGATTRS)} inform the correct hour (24h) without minutes: '))
    print(f'{colored("[FN][03]", "white", attrs=CGATTRS)} greet: {colored(greet(hr=hour), "red", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
    Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:
    Exemplo de entrada: telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
    Saida esperada: Todos os números foram convertidos corretamente!
    """
    def validate_phone_number(num: str) -> Tuple[int, str]:
        try:
            msg: str = ''
            assert num != 0
            n: int = int(num)
        except Exception as e:
            # print(f'{colored("[FN][04]", "white", attrs=CGATTRS)} Failed to convert to int: {num} :: {e}')
            msg = f'Failed to convert to int: {num} :: {e}'
            n = 0

        return n, msg

    def is_valid(phone: int) -> bool:
        return False if phone == 0 else True

    print(f'{colored("[FN][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    phones: List[str] = ["11987654321", "21912345678", "31987654321", "11911223344", "153238964X", "0"]
    for phone in phones:
        validated: Tuple[int, str] = validate_phone_number(num=phone)
        valid: bool = is_valid(phone=validated[0])

        print(f'{colored("[FN][04]", "white", attrs=CGATTRS)} valid: {colored(f"{phone:<15}", "yellow", attrs=CGATTRS)} {colored(valid, "magenta", attrs=CGATTRS)} {colored(validated[1], "red", attrs=CGATTRS)}')


def exerc_05() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][06]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][08]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][09]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


def exerc_10() -> None:
    """
    TODO start it
    """
    print(f'{colored("[FN][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][10]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')
