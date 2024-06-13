def lecture_02() -> None:
    number_00: float = float(input('inform number 01: '))
    number_01: float = float(input('inform number 02: '))
    number_02: float = float(input('inform number 03: '))

    print(f'sum of two {number_00} + {number_01} is: {number_00 + number_01}')
    print(f'sum of all three {number_00} + {number_01} + {number_02} is: {number_00 + number_01 + number_02}')  # noqa: E501
    print(f'difference from {number_00} - {number_01}: {number_00 - number_01}')  # noqa: E501
    print(f'mult {number_00} * {number_01}: {number_00 * number_01}')
    print(f"div {number_00} / {number_01} (second number {number_00} can't be null): {number_00 / number_01}")  # noqa: E501
    print(f'pot {number_00} ^ {number_01}: {number_00 ** number_01}')
    print(f'div int {number_00} // {number_01}: {number_00 // number_01}')
    print(f'remain {number_00} % {number_01}: {number_00 % number_01}')
    print(f'avarege ({number_00} + {number_01} {number_02}) / 3: {(number_00 + number_01 + number_02) / 3}')  # noqa: E501

    print(f'avg 5, 12, 20, 15: {(5 * 1) + (12 * 2) + (20 * 3) + (15 * 4) / 10}')  # noqa: E501

    phrase: str = 'Starting...'
    print(phrase)
    phrase = input('Inform some pharse here... ')
    print(phrase.upper())
    print(phrase.lower())
    my_phrase: str = '   MY   PHRASE   '
    print(my_phrase.strip())
    print(phrase.strip())
    print(phrase.strip().upper())
    print(phrase.strip().replace('e', 'f'))
    print(phrase.strip().replace('a', '@'))
    print(phrase.strip().replace('s', '$'))


def lecture_02b() -> None:
    avarage: float = 7.3
    result: str = 'NOT DONE'
    if avarage >= 7.00:
        result = 'DONE'

    print(f'result is: {result}')

    age_mary = int(input('Mary age: '))
    age_bia = int(input('Bia age: '))
    if age_mary > age_bia:
        print('Mary is older than Bia.')
    elif age_mary < age_bia:
        print('Bia is older than Mary.')

    employees_01 = int(input('Inform of totals of employees of company 01: '))
    employees_02 = int(input('Inform of totals of employees of company 02: '))
    if employees_01 >= employees_02:
        print('Company 01 has the same amount (or more) than company 02.')  # noqa: E501
    elif employees_01 <= employees_02:
        print('Company 01 has the same amount (or less) than company 02.')  # noqa: E501

    book_01 = input('Inform book 01: ')
    book_02 = input('Inform book 02: ')
    if book_01 == book_02:
        print('The title is equal!!')
    elif book_01 != book_02:
        print('The title is not equal!!')
