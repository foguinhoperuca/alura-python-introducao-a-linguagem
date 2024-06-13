from datetime import datetime
from typing import Any, List, Tuple


def lecture_00() -> None:
    print('Escola de Dados da Alura!')

    firstname: str = 'Jefferson'
    lastname: str = 'Campos'

    bday_day: int = 5
    bday_month: str = 'August'
    bday_year: int = 1986
    print(f'Name is......: {firstname}')
    print(f'Lastname is..: {lastname}')
    for letter in firstname:
        print(letter)

    print('-----------------------')
    res: List[Any] = [print(char) for char in lastname]
    print(res)
    print(bday_day, bday_month, bday_year)
    print('Actual year:', 2024)
    print('Better actual year:', datetime.now().year)
    print(type(res))
    print(type(firstname))
    print(type(bday_day))
    print(type(True))
    print(type(100.00))

    name = 'Fabricio Daniel'
    age = 15
    score = 8.45
    approved = True
    print(name, age, score, approved)

    job_salary: List[Tuple[str, int, float]] = [
        ('Segurança', 5, 3000.00),
        ('Docente', 16, 6000.00),
        ('Diretoria', 1, 12500.00),
    ]

    total_job: int = 0
    total_salary: float = 0.00

    for job in job_salary:
        total_job += job[1]
        total_salary += job[1] * job[2]

    avarage_salary: float = total_salary / total_job
    print(f'{avarage_salary=}')

    print(f'Total employee: {total_job}')
    print(f'Salary difference: {job_salary[2][2] - job_salary[0][2]}')
    print(f'cube of 2: {2**3}')
    print(f'module of 7 by 3: {7 % 3}')
    print(f'integer division 7 // 3: {7 // 3}')

    txt = '  Geovana Alessandra dias Sanyos '
    print(txt.upper())
    print(txt.lower())
    print(txt.strip().replace('y', 't'))
    print(chr(64), chr(79), chr(108), chr(225))

    student: str = 'Jose Sampaio'
    student_score: float = 7.5
    print('Student name: %s got %.3f.' % (student, student_score))
    another_student: str = 'Jose Carlos'
    another_student_age: int = 14
    print('Nome do aluno: {} age {}'.format(another_student, another_student_age))  # noqa: E501


def lecture_01() -> None:
    person_name: str = str(input('Please, inform your name: '))
    person_age: int = int(input('Please, inform your age: '))
    person_height: float = float(input('Please, inform your height (mts): '))
    print(f'Hello, {person_name}, you are {person_age} years old and has {person_height} mts.')  # noqa: E501

    nombre: str = input('Write your name here: ')
    print(f'Collected name was: {nombre}')

    year: int = int(input('Inform the YEAR of your birthday: '))
    print('Year is:', year, type(year))

    initial_score: float = float(input('Show your initial score: '))
    print('Initial score:', initial_score, type(initial_score))
