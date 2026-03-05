from datetime import datetime, time
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
    LIMIT: Decimal = round(Decimal('3000.00'))
    expenses: Decimal = round(Decimal(input('Inform your expenses: ')), 2)
    if expenses > LIMIT:
        print(f'Watch out! Your expenses ${expenses:.2f} supprass the limit ${LIMIT:.2f}')
    else:
        print(f'Your expenses ${expenses:.2f} is OK!')


def exerc_06() -> None:
    MIN_HOUR: time = time(hour=8, minute=0, second=0)
    MAX_HOUR: time = time(hour=18, minute=0, second=0)
    TIME_FMT: str = '%H:%M'

    entrace_time: time = datetime.strptime(input('Inform entrace time (HH:MM 24 hours): '), TIME_FMT).time()
    print(f'entrace time {entrace_time}')

    if entrace_time > MAX_HOUR or entrace_time < MIN_HOUR:
        print('Access denied!!')
    else:
        print('Access allowed!!')


def exerc_07() -> None:
    grade_01: Decimal = round(Decimal(input('Inform the first grade: ')), 2)
    grade_02: Decimal = round(Decimal(input('Inform the second grade: ')), 2)
    grade_03: Decimal = round(Decimal(input('Inform the third grade: ')), 2)
    avg: Decimal = (grade_01 + grade_02 + grade_03) / 3
    status: str = 'Failed'

    if avg >= 7.00:
        status = 'Approved'
    elif avg >= 5.00 and avg < 7.00:
        status = 'Under Review'
    else:
        status = 'Failed'

    print(f'For grades: {grade_01:.2f} {grade_02:.2f} {grade_03:.2f} with avarage {avg:.2f} make your status as *{status}*')


def exerc_08() -> None:
    distance: Decimal = round(Decimal(input('Inform the distance (KM): ')), 2)
    toll: Decimal = Decimal('10.00')

    if distance > Decimal('100.00') and distance <= Decimal('200.00'):
        toll = Decimal('20.00')
    elif distance > Decimal('200.00'):
        toll = Decimal('30.00')

    print(f'For your distance {distance:.2f} KM the toll will be ${toll:.2f}')


def exerc_09() -> None:
    game_number: int = int(input('Inform a number (integer): '))
    remainder: int = game_number % 2
    game_number_type: str = 'even'

    if remainder == 0:
        game_number_type = 'even'
    else:
        game_number_type = 'odd'

    print(f'The game number {game_number} has remainder {remainder} and is *{game_number_type}*')


def exerc_10() -> None:
    print('TODO must implement it!')
