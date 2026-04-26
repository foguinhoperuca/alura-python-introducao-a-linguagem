from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


def exerc_01():
    print(f'{colored("[LOOP][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    for client in ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']:
        print(f'[LOOP][]E01] client name: {client}')


def exerc_02():
    print(f'{colored("[LOOP][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    counter: int = 0
    while counter < 10:
        print(f'[LOOP][[E02]] working... {counter}')
        counter += 1


def exerc_03():
    print(f'{colored("[LOOP][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    counter: int = 1
    try:
        total: int = int(input('Inform the total of times to show message: '))
    except Exception as e:
        print(f'[LOOP][E03] Using default value: 1 --> {e}')
        total = 1
    finally:
        if total <= 0:
            total = 1

    while counter <= total:
        print(f'[LOOP][E03] WHILE: Welcome to ALURA Buscante for {counter}th time!')
        counter += 1

    print('----------')

    for i in range(total):
        print(f'[LOOP][E03] FOR: Welcome to ALURA Buscante for {i}th time!')


def exerc_04():
    print(f'{colored("[LOOP][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    sales: List[float] = [10.00, 20.00, 30.00, 40.00, 50.00]
    print(f'[LOOP][E04] Total sales is: ${sum(sales)}')

    total: float = 0.00
    for sale in sales:
        total += sale

    print(f'[LOOP][E04] Total sales loop: ${total}')


def exerc_05():
    print(f'{colored("[LOOP][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    name: str
    for project in ['website', 'game', 'data analysis', None, 'mobile app']:
        name = project if project is not None else '*** MISSING PROJECT ***'
        print(f'[LOOP][E05] PROJECT NAME..: {name}')


def exerc_06():
    print(f'{colored("[LOOP][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    TARGET: str = 'The Hobbit'
    books: List[str] = [
        '1984',
        'Dom Casmurro',
        'The Little Prince',
        TARGET,
        'Orgulho e Preconceito',
        'Memórias Póstumas de Brás Cubas'
    ]
    search: str = input('Inform the book name: ')

    for book in books:
        if search == TARGET:
            print(f'[LOOP][E06] Book found: {search} !!')
            break

    if search in books:
        print(f'[LOOP][E06] FYI: The book {search} searched is in our books collection.')


def exerc_07():
    print(f'{colored("[LOOP][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    INVENTORY: int = 5
    for item in range(INVENTORY):
        leftover = INVENTORY - (item + 1)
        if leftover >= 0:
            print(f'[LOOP][E07] [FOR] Selling done! [item: {item}] Still in inventory: {leftover}')

    print('-----')
    stock: int = INVENTORY
    while stock > 0:
        stock -= 1
        print(f'[LOOP][E07] [WHILE] Selling is done! Still in stock: {stock}')

    print('')
    print('[LOOP][E07] Inventory/Stock is over!!')


def exerc_08():
    print(f'{colored("[LOOP][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    COUNTDOWN: int = 10
    for final_countdown in range(COUNTDOWN, 0, -1):
        if final_countdown % 2 == 0:
            print(f"[LOOP][E08] Only {final_countdown} left - don't miss the promotion!!")
        else:
            print(f"[LOOP][E08] The countdown is going on: only {final_countdown} seconds.")

    print('[LOOP][E08] Go ahead and enjoy your promotion!!')


def exerc_09():
    print(f'{colored("[LOOP][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')

    books: List[str] = [
        {"name": "1984", "stock": 5},
        {"name": "Dom Casmurro", "stock": 0},
        {"name": "The Little Prince", "stock": 3},
        {"name": "The Hobbit", "stock": 0},
        {"name": "Orgulho e Preconceito", "stock": 2},
        {"name": "Memórias Póstumas de Brás Cubas", "stock": 7}
    ]

    for book in books:
        if book['stock'] == 0:
            continue

        print(f'[LOOP][E09] Book still available (stock: {book["stock"]}) :: {book["name"]}')
        # else:
        #     print(f'Book *** MISSING *** (stock: {book["stock"]}) :: {book["name"]}')


def exerc_10():
    print(f'{colored("[LOOP][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    USERNAME_MIN_LENGHT: int = 5
    PASSWORD_MIN_LENGHT: int = 8

    while True:
        username: str = input('[LOOP][E10] Inform your username..: ')
        password: str = input('[LOOP][E10] Inform your password..: ')

        if len(username) < USERNAME_MIN_LENGHT:
            print(f'[LOOP][E10] Your username {username} is invalid: it should contain at least {USERNAME_MIN_LENGHT} character (has {len(username)} characters)!!')
            continue

        if len(password) < PASSWORD_MIN_LENGHT:
            print(f'[LOOP][E10] Your password {password} is invalid: it should contain at least {PASSWORD_MIN_LENGHT} character (has {len(password)} characters)!!')
            continue

        print(f'[LOOP][E10] Username: {username} and password: *** successfully registered!!')
        break
