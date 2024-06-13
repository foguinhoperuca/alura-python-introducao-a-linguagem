from statistics import mean
from typing import List


def exercise_01() -> None:
    n01: float = float(input('Inform number 01: '))
    n02: float = float(input('Inform number 02: '))
    print(f'The bigest number is: {f"Number 01: {n01}" if n01 > n02 else f"Number 02: {n02}"}')  # noqa: E501


def exercise_02() -> None:
    growth: float = float(input('Inform the growth of your company (%): '))
    print(f'The growth was {"positive" if growth > 0 else "negative"}!!')


def exercise_03() -> None:
    letter: str = input('Inform a letter: ')
    print(f'The {letter} is {f"vogal" if letter in ["a", "e", "i", "o", "u"] else "consonant"}!!')  # noqa: E501


def exercise_04() -> None:
    car_year_01: float = float(input("Inform car's value in year 01: "))
    car_year_02: float = float(input("Inform car's value in year 02: "))
    car_year_03: float = float(input("Inform car's value in year 03: "))
    print(f'Avarage is: {mean([car_year_01, car_year_02, car_year_03])}; max is: {max([car_year_01, car_year_02, car_year_03])}; min is: {min([car_year_01, car_year_02, car_year_03])}')  # noqa: E501


def exercise_05() -> None:
    product_01: float = float(input("Inform product's value 01: "))
    product_02: float = float(input("Inform product's value 02: "))
    product_03: float = float(input("Inform product's value 03: "))
    min_value: float = product_01
    if product_02 < min_value:
        min_value = product_02

    if product_03 < min_value:
        min_value = product_03

    print(f'min value is: {min_value} - same as {min([product_01, product_02, product_03])}')  # noqa: E501


def exercise_06() -> None:
    number_01: float = float(input("Inform number 01: "))
    number_02: float = float(input("Inform number 02: "))
    number_03: float = float(input("Inform number 03: "))

    sorted_arr: List[float] = [number_01, number_02, number_03]
    sorted_arr.sort()
    print(f'Order is: {sorted_arr}')


def exercise_07() -> None:
    turn: str = input('Which is your turn [Morning | Afternoon | Night]')
    msg: str = 'Invalid input!'

    if turn.lower() == 'morning':
        msg = 'Good Morning, sunshine!'
    elif turn.lower() == 'afternoon':
        msg = 'Good afternoon, sir!'
    elif turn.lower() == 'night':
        msg = 'Night, night sweatheart!'

    print(msg)


def exercise_08() -> None:
    number: int = int(input('Give an integer number: '))
    print(f'Number is {"even" if (number % 2) == 0 else "odd"}')


def exercise_09() -> None:
    number: float = float(input('Give an number: '))
    breakpoint()
    print(f'Number is {"integer" if (number % 1) == 0 else "float"}')


def exercise_10() -> None:
    number_01: float = float(input("Inform number 01: "))
    number_02: float = float(input("Inform number 02: "))
    operation: str = input("Inform operation [+ | - | * | / | % | ** | //]: ")

    result: float = 0.0

    if operation == '+':
        result = number_01 + number_02
    elif operation == '-':
        result = number_01 - number_02
    elif operation == '*':
        result = number_01 * number_02
    elif operation == '/':
        result = number_01 / number_02
    elif operation == '%':
        result = number_01 % number_02
    elif operation == '**':
        result = number_01 ** number_02
    elif operation == '//':
        result = number_01 // number_02

    print(f'number 01 is {"even" if (number_01 % 2) == 0 else "odd"} {"positive" if number_01 >= 0 else "negative"} {"integer" if (number_01 % 1) == 0 else "float"}')  # noqa: E501
    print(f'number 02 is {"even" if (number_02 % 2) == 0 else "odd"} {"positive" if number_02 >= 0 else "negative"} {"integer" if (number_02 % 1) == 0 else "float"}')  # noqa: E501
    print(f'result is {"even" if (result % 2) == 0 else "odd"} {"positive" if result >= 0 else "negative"} {"integer" if (result % 1) == 0 else "float"}')  # noqa: E501


def exercise_11() -> None:
    pass


def exercise_12() -> None:
    pass


def exercise_13() -> None:
    pass
