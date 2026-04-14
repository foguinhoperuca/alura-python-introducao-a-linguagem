import re
from typing import List

from termcolor import colored


COLLORED_GENERAL_ATTRS: List[str] = ['bold', ]


def exerc_01() -> None:
    products: List[str] = [
        'ChocoLAte Branco',
        'ChoColate Negro',
        'BoLaChA',
        'CaFé',
        'LEIte',
        '    Arroz IntegRAl',
        'Óleo      de SojA',
        'Bandeija de       Ovos',
        'Margarina seM SaL          ',
    ]
    print('[REGEXP] exerc_01')
    custom: str = input('Inform a custom product: ')
    products.insert(0, custom)

    for product in products:
        p: str = re.sub(r'\s{2,}', ' ', product.strip().lower())
        print(f'[REGEX][01] product fixed "{p}" :: original "{product}"')


def exerc_02() -> None:
    print('[REGEXP] exerc_02')
    name: str = input('Inform your name: ')
    city: str = input('Inform your city: ')
    print(f'[REGEX][02] Hello, {name}! Welcome to system of {city}.')


def exerc_03() -> None:
    print('[REGEXP] exerc_03')
    words: List[str] = [
        'Misterioso',
        'Respanwing',
        'Mana',
        'Health',
        'Objectives',
        'Magic Items',
        'Main Character',
        'NPC'
    ]
    keyword: str = input('Inform a keyword: ')
    words.insert(0, keyword)
    for word in words:
        start: str = word[0:3]
        end: str = word[-3:]
        print(f'[REGEX][03] ORIGINAL: {colored(word, 'yellow', attrs=COLLORED_GENERAL_ATTRS)} :: START {colored(start, 'magenta', attrs=COLLORED_GENERAL_ATTRS)} :: END {colored(end, 'blue', attrs=COLLORED_GENERAL_ATTRS)}')


def exerc_04() -> None:
    print('[REGEXP] exerc_04')
    urls: List[str] = [
        'https://google.com',
        'https://kernel.org',
        'http://microsoft.com',
        'https://alura.com.br',
        'http://jeffersoncampos.eti.br',
        'https://python.org',
        'https://apple.com',
        'https://aws.amazon.com',
        'https://openai.com',
        'https://youtube.com',
        'https://web.whatsapp.com'
    ]
    custom_url: str = input('Inform a custom url to be validate: ')
    urls.insert(0, custom_url)
    for url in urls:
        valid: str = colored(False, 'red', attrs=COLLORED_GENERAL_ATTRS)
        if url.startswith('https://') and url.endswith('.com'):
            valid = colored(True, 'blue', attrs=COLLORED_GENERAL_ATTRS)

        print(f'[REGEX][04] ORIGINAL: {colored(url, 'yellow', attrs=COLLORED_GENERAL_ATTRS)} :: VALID {valid}')


def exerc_05() -> None:
    print('[REGEXP] exerc_05')
    prescriptions: List[str] = [
        'A receita 1087568 foi enviada pelo cliente.',
        'A receita 86592217 não possui remédios em estoque.',
        'Diclofenato de Potássio está em falta e a receita 92734 não poderá ser atendida no momento.',
        'Uma nova remessa de Dipirona foi enviada para atender a receita 463284.',
        'As receitas 158926 e 88462 serão atendidas imediatamente. A receita 947 e 37349 tem a previsão de atendimento amanhão. As demais receitas ainda não tem previsão de atendimento.'
    ]
    custom_prescription: str = input('Inform a custom prescription to be validate: ')
    prescriptions.insert(0, custom_prescription)
    for prescription in prescriptions:
        numbers: List[str] = re.findall(r'\d+', prescription)
        print(f'[REGEX][05] ORIGINAL: {colored(prescription, 'yellow', attrs=COLLORED_GENERAL_ATTRS)}')

        for number in numbers:
            print(f'[REGEX][05] prescription found: {colored(number, 'red', attrs=COLLORED_GENERAL_ATTRS)}')

        print('**********************')


def exerc_06() -> None:
    print('[REGEXP][E06] exerc_06')
    phrases: List[str] = [
        'O dia está bom, tudo está bom.'
    ]
    custom_phrase: str = input('Inform a custom phrase: ')
    bad_word: str = input('Inform the word that must be removed: ')
    good_word: str = input('Inform the new desired word: ')
    phrases.insert(0, custom_phrase)
    for phrase in phrases:
        new_phrase_replace: str = colored(phrase, 'yellow', attrs=COLLORED_GENERAL_ATTRS)
        new_phrase_replace = new_phrase_replace.replace(bad_word, colored(good_word, 'red', attrs=COLLORED_GENERAL_ATTRS))
        new_phrase_regex: str = phrase
        new_phrase_regex = re.sub(rf'\b{bad_word}\b', colored(good_word, 'magenta', attrs=COLLORED_GENERAL_ATTRS), new_phrase_regex)
        # new_phrase_regex: str = colored(phrase, 'blue', attrs=COLLORED_GENERAL_ATTRS)
        # new_phrase_regex = re.sub(rf'\b{bad_word}\b', good_word, new_phrase_regex)
        print(f'[REGEX][06][REPLACE] ORIGINAL: {colored(phrase, 'white', attrs=COLLORED_GENERAL_ATTRS)} :: NEW {new_phrase_replace}')
        print(f'[REGEX][06][REGEX] ORIGINAL: {colored(phrase, 'white', attrs=COLLORED_GENERAL_ATTRS)} :: NEW {new_phrase_regex}')


def exerc_07() -> None:
    print('[REGEXP] exerc_07')
    names: List[str] = [
        'maria123',
        'Jeff Fields',
        'Jhon Snow',
        'Paul Jr. X',
        'Chiu Sey2 Han',
        'Mark humble'
    ]
    custom_name: str = input('Inform a custom name: ')
    names.insert(0, custom_name)
    for name in names:
        valid: bool = True
        numbers: List[str] = re.findall(r'\d+', name)
        first_letter: str = re.findall(r'[A-Z]', name[0])
        if numbers or not first_letter:
            valid = False

        full_match_valid: bool = re.fullmatch(r'[A-Z][a-z]*', name) is not None
        valid_multiple_names: bool = re.fullmatch(r'[A-Z][\w]*', name) is not None

        print(f'[REGEX][07] ORIGINAL: {colored(name, 'white', attrs=COLLORED_GENERAL_ATTRS)} :: VALID {colored(valid, 'red', attrs=COLLORED_GENERAL_ATTRS)} :: FULLMATCH {colored(full_match_valid, 'blue', attrs=COLLORED_GENERAL_ATTRS)} :: ANOTHER {colored(valid_multiple_names, 'green', attrs=COLLORED_GENERAL_ATTRS)}')


def exerc_08() -> None:
    print('[REGEXP] exerc_08')
    print('[REGEX][08] TODO implement it!!')


def exerc_09() -> None:
    print('[REGEXP] exerc_09')
    print('[REGEX][09] TODO implement it!!')


def exerc_10() -> None:
    print('[REGEXP] exerc_10')
    print('[REGEX][10] TODO implement it!!')
