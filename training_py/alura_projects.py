import logging
import re
import random
import string
from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]
LOG_FORMAT_SIMPLE = colored('[%(levelname)s]', 'red', attrs=['bold', 'dark']) + ' %(message)s'  # noqa: E501
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT_SIMPLE)


def class02() -> None:
    print(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} custom code')
    phrase: str = input(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} inform a phrase:\n')
    words: List[str] = phrase.split(' ')
    print(f'{colored("[PROJECTS][class02]", "white", attrs=CGATTRS)} total words: {len(words)}')


def exerc_01() -> None:
    """
    João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
    Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
    Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
    Exemplo de entrada:
    > Digite o valor da conta: 120.00
    > Digite a porcentagem de gorjeta: 10
    Saída esperada:
    > Valor da gorjeta: R$ 12.00
    > Total a pagar: R$ 132.00
    """
    print(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    value: float = float(input(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} inform the value: $'))
    tip_percentage: float = float(input(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} inform tip percentage: %'))
    tip: float = value * (tip_percentage / 100)
    total: float = value + tip
    print(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} value {colored(f"${value:.2f}", "red", attrs=CGATTRS)} tip percentage {colored(f"{tip_percentage:.2f} %", "magenta", attrs=CGATTRS)} total tip {colored(f"${tip:.2f}", "yellow", attrs=CGATTRS)} final value: {colored(f"${total:.2f}", "cyan", attrs=CGATTRS)}')


def exerc_02() -> None:
    """
    Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
    Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.
    Exemplo de entrada: Digite seu CPF: 12345678901
    Saída esperada: CPF válido.
    Se for inválido:
    Digite seu CPF: 1234abc567
    Erro: O CPF deve conter apenas números.
    Se o CPF tiver um número de dígitos diferente de 11:
    Digite seu CPF: 1234567
    Erro: O CPF deve ter exatamente 11 dígitos.
    """
    def cpf_has_only_valid_character(document: str) -> bool:
        chars: List[str] = re.findall(r'[A-Z][a-z]*', document)
        logging.debug(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} {chars=}')
        if chars:
            print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} invalid cpf character!!')
            return False
        return True

    def cpf_valid_lenght(document: str) -> bool:
        if len(document) != 11:
            print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} invalid cpf lenght!!')
            return False
        return True

    print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    cpf: str = input(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} inform the document number (CPF): ')
    is_valid: bool = cpf_has_only_valid_character(document=cpf) and cpf_valid_lenght(document=cpf)

    print(f'{colored("[PROJECTS][02]", "white", attrs=CGATTRS)} cpf {colored(cpf, "yellow", attrs=CGATTRS)} is valid: {colored(is_valid, "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.
    Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
    Exemplo de entrada: Digite um texto: A linguagem Python é muito versátil.
    Saída esperada: O texto contém 13 vogais.
    """
    def count_vowel(word: str) -> int:
        return len([c for c in word.lower() if c in ['a', 'e', 'i', 'o', 'u']])

    print(f'{colored("[PROJECTS][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    word: str = input(f'{colored("[PROJECTS][03]", "white", attrs=CGATTRS)} Inform the word: ')
    print(f'{colored("[PROJECTS][03]", "white", attrs=CGATTRS)} lenght of vowel: {colored(count_vowel(word=word), "red", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.
    Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
    Exemplo de entrada:
    > Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
    Saída esperada:
    > Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais
    > Se nenhum palavra longa for encontrada: Nenhuma palavra longa foi encontrada no texto.
    """
    def get_long_words(phrase: str) -> List[str] | str:
        long_words: List[str] = [w for w in phrase.split(' ') if len(w) >= 10]

        return long_words if len(long_words) > 0 else 'No long words found in text!!'

    phrases: List[str] = [
        'A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais',
        'Algum teste sem palavras longas'
    ]
    print(f'{colored("[PROJECTS][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    for phrase in phrases:
        print(f'{colored("[PROJECTS][04]", "white", attrs=CGATTRS)} long words: {colored(get_long_words(phrase=phrase), "red", attrs=CGATTRS)}')


def exerc_05() -> None:
    """
    Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.
    Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.
    Saída esperada: Senha gerada: A1b@C3d$E5f&
    """
    PHROHIBITED_CHARACTERS: List[str] = [' ']
    MINIMUM_PASSOWRD_SIZE: int = 12

    def generate_password(size: int = MINIMUM_PASSOWRD_SIZE, not_allowed_characters: List[str] = PHROHIBITED_CHARACTERS) -> str:
        assert size >= MINIMUM_PASSOWRD_SIZE

        lower_charcter: str = random.choices([c for c in string.ascii_lowercase if c not in not_allowed_characters and c not in PHROHIBITED_CHARACTERS], k=1)
        upper_charcter: str = random.choices([c for c in string.ascii_uppercase if c not in not_allowed_characters and c not in PHROHIBITED_CHARACTERS], k=1)
        digit_charcter: str = random.choices([c for c in string.digits if c not in not_allowed_characters and c not in PHROHIBITED_CHARACTERS], k=1)
        punctuation_charcter: str = random.choices([c for c in string.punctuation if c not in not_allowed_characters and c not in PHROHIBITED_CHARACTERS], k=1)
        characters: str = [c for c in string.ascii_letters + string.digits + string.punctuation if c not in not_allowed_characters and c not in PHROHIBITED_CHARACTERS and c not in lower_charcter and c not in upper_charcter and c not in digit_charcter and c not in punctuation_charcter]
        generated_password: str = f'{lower_charcter[0].replace("\'", "")}{upper_charcter[0].replace("\'", "")}{digit_charcter[0].replace("\'", "")}{punctuation_charcter[0].replace("\'", "")}' + ''.join(random.choices(characters, k=size - 4))

        assert all([True if c not in not_allowed_characters else False for c in generated_password])

        print(f'{generated_password=} :: {lower_charcter=}')

        return "".join(random.sample(generated_password, len(generated_password)))

    print(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    size_password: int = -1
    try:
        size_password = int(input(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} Inform the minimum size of characters: '))
        assert size_password >= MINIMUM_PASSOWRD_SIZE
    except Exception as e:
        print(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} Invalid password size: {size_password=} :: {e}')
        size_password = MINIMUM_PASSOWRD_SIZE

    unwanted_characters: str = input(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} Inform a list of unwanted charcters: ')
    not_allowed_characters: List[str] = [u for u in unwanted_characters] + PHROHIBITED_CHARACTERS
    password: str = generate_password(size=size_password if size_password >= MINIMUM_PASSOWRD_SIZE else MINIMUM_PASSOWRD_SIZE, not_allowed_characters=not_allowed_characters)
    print(f'{colored("[PROJECTS][05]", "white", attrs=CGATTRS)} password generated {colored(password, "yellow", attrs=CGATTRS)} :: size used: {colored(size_password, "cyan", attrs=CGATTRS)} (MINIMUM: {colored(MINIMUM_PASSOWRD_SIZE, "magenta", attrs=CGATTRS)}) :: unwanted characters: {colored(unwanted_characters, "red", attrs=CGATTRS)} :: PHROHIBITED CHARACTERS {colored(PHROHIBITED_CHARACTERS, "white", attrs=CGATTRS)} ')


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
