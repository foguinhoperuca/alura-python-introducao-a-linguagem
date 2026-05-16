from enum import auto, Enum
import logging
import re
import random
import string
from typing import Dict, List, Tuple

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


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
    Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.
    Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:
    - Pedra ganha de Tesoura (Pedra quebra Tesoura);
    - Tesoura ganha de Papel (Tesoura corta Papel);
    - Papel ganha de Pedra (Papel cobre Pedra);
    - Se ambos escolherem a mesma opção, é um empate.
    Exemplo de entrada:
    > Escolha: pedra, papel ou tesoura? papel
    Saída esperada:
    > Computador escolheu: pedra
    > Você venceu!
    Caso o computador vença:
    > Computador escolheu: tesoura
    > Você perdeu!
    Caso o computador escolha a mesma opção que você:
    > Computador escolheu: papel
    > Empate!
    """
    class JokenPoPower(Enum):
        ROCK = auto()
        PAPER = auto()
        SCISSORS = auto()

    class Result(Enum):
        LOSS = 0
        DRAW = 0.5
        WINS = 1

    def fight(player: JokenPoPower, enemy: JokenPoPower) -> Result:
        """
        Define the result of fight of player against enemy.
        """
        if player == enemy:
            return Result.DRAW

        if player is JokenPoPower.ROCK:
            if enemy == JokenPoPower.PAPER:
                return Result.LOSS
            elif enemy == JokenPoPower.SCISSORS:
                return Result.WINS
        elif player is JokenPoPower.PAPER:
            if enemy == JokenPoPower.SCISSORS:
                return Result.LOSS
            elif enemy == JokenPoPower.ROCK:
                return Result.WINS
        elif player is JokenPoPower.SCISSORS:
            if enemy == JokenPoPower.ROCK:
                return Result.LOSS
            elif enemy == JokenPoPower.PAPER:
                return Result.WINS

    score: float = 0
    enemy_score: float = 0
    max_point: float = 3.0
    print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} ---------- MAX SCORE {colored(max_point, "blue", attrs=CGATTRS)} ----------')
    while True:
        if score >= max_point or enemy_score >= max_point:
            print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} max score reached: {colored(max_point, "blue", attrs=CGATTRS)}')
            break

        choosed: int = int(input(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} Choose your power by number (0 - STOP): {[f"{p.value} - {p.name}" for p in JokenPoPower]} '))
        if choosed == 0:
            break

        you: JokenPoPower = JokenPoPower(choosed)
        computer: JokenPoPower = JokenPoPower(random.randint(1, 3))
        result: Result = fight(player=you, enemy=computer)
        score += result.value
        match result:
            case Result.WINS:
                enemy_score += Result.LOSS.value
            case Result.DRAW:
                enemy_score += Result.DRAW.value
            case Result.LOSS:
                enemy_score += Result.WINS.value

        print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
        print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} player 1 choosed..: {colored(you.name, "cyan", attrs=CGATTRS)}')
        print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} player 2 choosed..: {colored(computer.name, "magenta", attrs=CGATTRS)}')
        print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} results are.......: {colored(f"{result.value}", "yellow", attrs=CGATTRS)} {colored(f"[{result.name}]", "red", attrs=CGATTRS)}')
        print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} score are.........: {colored(f"you {score}", "cyan", attrs=CGATTRS)} {colored(f"enemy {enemy_score}", "magenta", attrs=CGATTRS)}')

    print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} ---------- FINAL SCORE ----------')
    print(f'{colored("[PROJECTS][06]", "white", attrs=CGATTRS)} Final score are: {colored(f"you {score}", "cyan", attrs=CGATTRS)} {colored(f"enemy {enemy_score}", "magenta", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.
    Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.
    Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .
    Exemplo de entrada:
    > Tente adivinhar o número (1-100): 50
    Saída esperada:
    > Parabéns! Você acertou o número 37.
    Caso o número esteja abaixo:
    > Muito baixo! Tente novamente: 17
    Agora, caso esteja acima:
    > Muito alto! Tente novamente: 75
    Em caso de exceção:
    > Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.
    > Entrada inválida: invalid literal for int() with base 10: 'abc12'.'
    """
    print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    MAX: int = 100
    counter: int = 0
    result: str = ''
    secret: int = random.randint(1, MAX)
    found: bool = False
    while not found:
        counter += 1
        try:
            guess: int = int(input(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} Inform a number (MAX {colored(MAX, "magenta", attrs=CGATTRS)}): '))
            if guess < 0 or guess > MAX:
                raise ValueError(f'Value out of range than 0 to MAX ({MAX}): {guess}')
        except Exception as e:
            print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} invalid number: {colored(e, "red", attrs=CGATTRS)}')
            continue

        if guess == 0:
            print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} I gave up!! Secret is: {colored(secret, "yellow", attrs=CGATTRS)}')
            break

        if guess == secret:
            result = 'FOUND'
            found = True
        elif guess > secret:
            result = 'guess is BIGGER'
        else:
            result = 'guess is LOWER'

        print(f'{colored("[PROJECTS][07]", "white", attrs=CGATTRS)} result: {colored(result, "cyan", attrs=CGATTRS)} counter: {colored(counter, "blue", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
    Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
    Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
    Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
    Exemplo de entrada:
    > Digite o primeiro número: 5
    > Escolha a operação (+, -, *, /): +
    > Digite o segundo número: 7
    Saída esperada:
    > Resultado: 12
    Caso selecione nenhuma das operações listadas:
    > Opção inválida
    Caso digite um caractere em vez de número:
    > Erro: Entrada inválida. Digite apenas números.
    Caso tente fazer uma divisão por 0:
    > Erro: Divisão por zero não é permitida.
    """
    calculate = lambda lt, rt, op: float(eval(f'{lt}{op}{rt}'))  # noqa: E731
    OPERATORS: Tuple[str] = ('+', '-', '*', '/')
    print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')

    left: float | None = None
    while left is None:
        try:
            left = float(input(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} Inform the left term...: '))
        except ValueError as e:
            print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} gota error: {colored(e, "red", attrs=CGATTRS)}')
            left = None

    right: float | None = None
    while right is None:
        try:
            right = float(input(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} Inform the right term..: '))
            if right == 0:
                raise ZeroDivisionError("Right member can't be zero!")
        except (ValueError, ZeroDivisionError) as e:
            print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} gota error: {colored(e, "red", attrs=CGATTRS)}')
            right = None

    operator: str | None = None
    while operator is None:
        operator = input(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} Inform the operand.....: ')
        if operator not in OPERATORS:
            operator = None
            print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} invalid operator. It should be one of {colored(OPERATORS, "red", attrs=CGATTRS)}')

    print(f'{colored("[PROJECTS][08]", "white", attrs=CGATTRS)} {colored(left, "red", attrs=CGATTRS)} {colored(operator, "cyan", attrs=CGATTRS)} {colored(right, "yellow", attrs=CGATTRS)} = {colored(calculate(lt=left, rt=right, op=operator), "magenta", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.
    Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
    Exemplo de entrada:
    > 1. Adicionar tarefa
    > 2. Visualizar tarefas
    > 3. Remover tarefa
    > 4. Sair
    > Escolha uma opção: 1
    Saída esperada:
    > Digite a tarefa: Estudar Python
    > Tarefa adicionada!
    Caso selecione a opção 2 ao adicionar uma tarefa:
    > Tarefas:
    > 1. Estudar Python
    Caso selecione a opção 3 com uma tarefa adicionada:
    > Digite o número da tarefa a ser removida: 1
    > Tarefa 'Estudar Python' removida!
    Caso selecione a opção 3 sem uma tarefa adicionada:
    > Digite o número da tarefa a ser removida: Estudar Python
    > Erro: Nenhuma tarefa para remover.
    Caso selecione a opção 3 com uma opção inválida:
    > Escolha uma opção: 3
    > Digite o número da tarefa a ser removida: ABC
    > Erro: Entrada inválida! Digite um número.
    Caso selecione nenhuma das opções listadas:
    > Escolha uma opção: 5
    > Erro: Opção inválida! Escolha uma opção entre 1 e 4.
    Caso selecione a opção 4:
    > Escolha uma opção: 4
    > Saindo do gerenciador de tarefas. Até mais!
    """
    print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')

    def add(task: str) -> None:
        TASKS.append(task)
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Task added: {colored(f"{task}", "yellow", attrs=CGATTRS)}')

    def remove(index: int) -> str:
        assert isinstance(index, int)
        TASKS.pop(index)

    def show(index: int) -> None:
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored(f"{index}", "cyan", attrs=CGATTRS)}. {TASKS[index]}')

    TASKS: List[str] = []
    option: str | None = ''
    while option is not None:
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Alura TUI Task Manager {colored("Training Python: Projects", "cyan", attrs=CGATTRS)}')
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored("A. ADD", "yellow", attrs=CGATTRS)} a Task;')
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored("S. SHOW", "blue", attrs=CGATTRS)} a Task;')
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored("R. REMOVE", "red", attrs=CGATTRS)} a Task;')
        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored("E. Bye!", "magenta", attrs=CGATTRS)} Go home!;')

        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored("TASKS:", "cyan", attrs=CGATTRS)}')
        for i, t in enumerate(TASKS):
            print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored(f"{i}", "cyan", attrs=CGATTRS)}. {t}')

        option = input(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Your option: ')
        match option.upper():
            case 'A':
                task: str = input(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Inform the task: ')
                add(task=task)
            case 'S':
                index = int(input(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Inform the index of task: '))
                show(index=index)
            case 'R':
                try:
                    if len(TASKS) == 0:
                        raise ValueError('The size of TASKS is 0! Can not delete any task.')

                    index = int(input(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} Inform the index of task: '))
                    remove(index=index)
                except Exception as e:
                    print(f'{colored("[PROJECTS][01]", "white", attrs=CGATTRS)} got some error: {colored(f"{e}", "red", attrs=CGATTRS)}')
            case 'E':
                print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} As te la {colored("Bye, Bye!", "magenta", attrs=CGATTRS)}')
                option = None
            case _:
                print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} {colored(f"Option invalid: {option}", "red", attrs=CGATTRS)}')

        print(f'{colored("[PROJECTS][09]", "white", attrs=CGATTRS)} ---------- {colored(f"E09", "red", attrs=CGATTRS)} ----------')


def exerc_10() -> None:
    """
    Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
    Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.
    Exemplo de entrada:
    > Digite o valor do saque: 188
    Saída esperada:
    Cédulas entregues:
    > 1 de R$ 100
    > 1 de R$ 50
    > 1 de R$ 20
    > 1 de R$ 10
    > 1 de R$ 5
    > 1 de R$ 2
    Caso faça um saque de valor não inválido (ímpar):
    > Erro: O valor deve ser múltiplo de 2.
    """
    def get_banknotes(vl: int) -> Dict[int, int]:
        remainder: int = vl
        banknotes: Dict[int, int] = {
            200: 0,
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0
        }

        for banknote in banknotes.keys():
            if banknote > remainder:
                logging.debug(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} {banknote=}')
                continue

            if (remainder % banknote) % 2 > 0:
                logging.info(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} Not using banknote ${colored(banknote, "cyan", attrs=CGATTRS)} (odd banknote) because the remainder after will be odd!')
                continue

            banknotes[banknote] = remainder // banknote
            remainder = remainder % banknote
            logging.debug(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} {banknote=} {banknotes[banknote]=} {remainder=}')

        return banknotes

    print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')

    while True:
        try:
            value: int = int(input(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} Inform the value. There is no banknotes of value $1, so, only even values are accepted (inform 0 or negative to end the program): '))
            if value <= 0:
                print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} {colored("Bye", "red", attrs=CGATTRS)}')
                break

            if value % 2 == 1:
                raise ValueError(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} unacepted value: ${colored(value, "magenta", attrs=CGATTRS)} - it should be even and greater than zero!!')

            print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} total banknotes for value {colored(f"${value}", "blue", attrs=CGATTRS)} -> {colored(get_banknotes(vl=value), "yellow", attrs=CGATTRS)}')
        except Exception as e:
            print(f'{colored("[PROJECTS][10]", "white", attrs=CGATTRS)} ERROR: {colored(e, "red", attrs=CGATTRS)}')
