from typing import List


def exerc_01():
    print('[LOOP] exerc_01')
    for client in ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']:
        print(f'[LOOP_E01] client name: {client}')


def exerc_02():
    print('[LOOP] exerc_02')
    counter: int = 0
    while counter < 10:
        print(f'[LOOP][[E02]] working... {counter}')
        counter += 1


def exerc_03():
    print('[LOOP] exerc_03')
    counter: int = 1
    try:
        total: int = int(input('Inform the total of times to show message: '))
    except Exception as e:
        print(f'Using default value: 1 --> {e}')
        total = 1
    finally:
        if total <= 0:
            total = 1

    while counter <= total:
        print(f'WHILE: Welcome to ALURA Buscante for {counter}th time!')
        counter += 1

    print('----------')

    for i in range(total):
        print(f'FOR: Welcome to ALURA Buscante for {i}th time!')


def exerc_04():
    print('[LOOP] exerc_04')
    sales: List[float] = [10.00, 20.00, 30.00, 40.00, 50.00]
    print(f'Total sales is: ${sum(sales)}')

    total: float = 0.00
    for sale in sales:
        total += sale

    print(f'Total sales loop: ${total}')


def exerc_05():
    print('[LOOP] exerc_05')
    name: str
    for project in ['website', 'game', 'data analysis', None, 'mobile app']:
        name = project if project is not None else '*** MISSING PROJECT ***'
        print(f'PROJECT NAME..: {name}')


def exerc_06():
    print('[LOOP] TODO implement exerc_06')


def exerc_07():
    print('[LOOP] TODO implement exerc_07')


def exerc_08():
    print('[LOOP] TODO implement exerc_08')


def exerc_09():
    print('[LOOP] TODO implement exerc_09')


def exerc_10():
    print('[LOOP] TODO implement exerc_10')
