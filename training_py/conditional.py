from decimal import Decimal


def exerc_01() -> None:
    apples: int = int(input("How many apples was sold? "))
    bananas: int = int(input("How many bananas was sold? "))
    winner: str = ""

    if apples > bananas:
        winner = "apples"
    elif apples == bananas:
        winner = "same quantity"
    else:
        winner = "bananas"

    print(f"Winner is: {winner}")


def exerc_02() -> None:
    project_a: int = int(input("How many day for project A? "))
    project_b: int = int(input("How many day for project B? "))
    project_c: int = int(input("How many day for project C? "))
    msg: str = "Data input OK!!"

    if project_a < 0 or project_b < 0 or project_c < 0:
        msg = "Days must be positive!!"

    print(msg)


def exerc_03() -> None:
    temperature: int = int(input('Enter the temperature: '))
    if temperature > 25:
        print(f'Too hot at {temperature}°!!')
    else:
        print(f'Good to go at {temperature}°')


def exerc_04() -> None:
    print('TODO must implement it!')
    weight: Decimal = round(Decimal(input('Inform your weight: ')), 2)
    height: Decimal = round(Decimal(input('Inform your height: ')), 2)
    imc: Decimal = weight / (height ** 2)
    status: str = 'UNDERWEIGHT'
    if imc >= 18.5 and imc < 25:
        status = 'NORMAL'
    elif imc >= 25:
        status = 'OVERWEIGHT'

    print(f'Your IMC is: {imc:.2f} and you are: {status}')


def exerc_05() -> None:
    print('TODO must implement it!')


def exerc_06() -> None:
    print('TODO must implement it!')


def exerc_07() -> None:
    print('TODO must implement it!')


def exerc_08() -> None:
    print('TODO must implement it!')


def exerc_09() -> None:
    print('TODO must implement it!')


def exerc_10() -> None:
    print('TODO must implement it!')
