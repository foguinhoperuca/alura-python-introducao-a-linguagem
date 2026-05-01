from typing import Callable, List, Set, Tuple
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
    Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.
    Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
    Exemplo de entrada: Digite os valores das vendas: 100 250 300
    Saída esperada: O total de vendas foi: 650
    """
    def process(vls: str) -> float:
        try:
            return sum([float(vl) for vl in list(vls.split(' '))])
        except Exception as e:
            print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} error with input: {colored(vls, "yellow", attrs=CGATTRS)} :: {colored(e, "red", attrs=CGATTRS)}')
            return 0.00

    def process_map(vls: str) -> float:
        try:
            return sum(map(float, vls.split(' ')))
        except Exception as e:
            print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} error with input: {colored(vls, "yellow", attrs=CGATTRS)} :: {colored(e, "red", attrs=CGATTRS)}')
            return 0.00

    print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    values: str = input(f'{colored("[FN][05]", "white", attrs=CGATTRS)} inform a list of sales sperated by space: ')
    print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} [PROCESS] total sales..: {colored(f"${process(values)}", "magenta", attrs=CGATTRS)}')
    print(f'{colored("[FN][05]", "white", attrs=CGATTRS)} [MAP] total sales......: {colored(f"${process_map(values)}", "cyan", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
    Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
    Exemplo de entrada: Digite os números separados por espaço: 1 2 3 4 5 6
    Saída esperada: Números pares: 2 4 6
    """
    def odd_filter(nums: Set[int]) -> List[int]:
        return list(filter(lambda x: x % 2 == 0, nums))

    print(f'{colored("[FN][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    numbers: List[int] = [1, 2, 3, 4, 5, 6]
    user_numbers: str = input(f'{colored("[FN][06]", "white", attrs=CGATTRS)} Inform a list of numbers to append (separeted by ;): ')
    elements: Set[int] = set(numbers + list(map(int, user_numbers.split(';'))))
    print(f'{colored("[FN][06]", "white", attrs=CGATTRS)} odd numbers {colored(odd_filter(nums=elements), "red", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
    Crie um programa que junte as listas e exiba o resultado no formato produto: preço
    Exemplo de entrada:
    > Digite os produtos separados por vírgula: maçã, banana, pera
    > Digite os preços separados por vírgula: 2.5, 1.2, 3.0
    Saída esperada:
    > maçã: 2.5
    > banana: 1.2
    > pera: 3.0
    """
    def union_elements(pro: List[str], pri: List[float]) -> List[Tuple[str, float]]:
        return zip(products, prices)

    print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    products: List[str] = ['maçã', 'banana', 'pera']
    prices: List[float] = [2.5, 1.2, 3.0]
    print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} products..: {colored([f"{p:^6}" for p in products], "red", attrs=CGATTRS)}')
    print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} prices....: {colored([f"{p:^6}" for p in prices], "yellow", attrs=CGATTRS)}')
    for item in union_elements(pro=products, pri=prices):
        print(f'{colored("[FN][07]", "white", attrs=CGATTRS)} item {colored(item[0], "red", attrs=CGATTRS)}: {colored(item[1], "yellow", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
    Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
    Exemplo de entrada:
    > Digite o primeiro número: 10
    > Digite o segundo número: 5
    > Escolha a operação (| + | - | * | / |): +
    Saída esperada: O resultado é: 15
    """
    calculate = lambda lt, rt, op: float(eval(f'{lt}{op}{rt}'))  # noqa: E731

    print(f'{colored("[FN][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    left: float = float(input(f'{colored("[FN][08]", "white", attrs=CGATTRS)} Inform the left term...: '))
    right: float = float(input(f'{colored("[FN][08]", "white", attrs=CGATTRS)} Inform the right term..: '))
    operator: str = input(f'{colored("[FN][08]", "white", attrs=CGATTRS)} Inform the operand.....: ')
    print(f'{colored("[FN][08]", "white", attrs=CGATTRS)} {colored(left, "red", attrs=CGATTRS)} {colored(operator, "cyan", attrs=CGATTRS)} {colored(right, "yellow", attrs=CGATTRS)} = {colored(calculate(lt=left, rt=right, op=operator), "magenta", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
    Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.
    Exemplo de entrada:
    > Digite a porcentagem de desconto: 10
    > Digite o valor da compra: 200
    Saída esperada: Preço final com desconto: 180.0
    """
    def discount(rate: float) -> Callable:
        def apply(value: float) -> float:
            return value * rate
        return apply

    print(f'{colored("[FN][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    price: float = float(input(f'{colored("[FN][09]", "white", attrs=CGATTRS)} Inform the original price: '))
    discount_rate: float = float(input(f'{colored("[FN][09]", "white", attrs=CGATTRS)} Inform the discount rate: '))
    percent_discount: Callable = discount(rate=discount_rate)
    discount_value: float = percent_discount(value=price)
    total: float = price - discount_value
    print(f'{colored("[FN][09]", "white", attrs=CGATTRS)} {colored(f"${price} (full price)", "magenta", attrs=CGATTRS)} {colored("-", "red", attrs=CGATTRS)} {colored(f"${discount_value} (discount value)", "yellow", attrs=CGATTRS)} = {colored(f"${total} (total)", "cyan", attrs=CGATTRS)}')


def exerc_10() -> None:
    """
    Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
    Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
    Exemplo de entrada: Digite um número: 5
    Saída esperada: A soma de 1 a 5 é: 15
    """
    def factorial(n: int) -> int:
        if n == 1:
            return 1
        return n + factorial(n - 1)

    number: int = int(input(f'{colored("[FN][10]", "white", attrs=CGATTRS)} inform the number: '))
    print(f'{colored("[FN][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[FN][10]", "white", attrs=CGATTRS)} factorial for {colored(number, "yellow", attrs=CGATTRS)} is {colored(factorial(n=number), "red", attrs=CGATTRS)}')
