from typing import List, Tuple

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


def exerc_01() -> None:
    """
    Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.
    Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
    Exemplo de Entrada:
        Digite o item que você quer verificar: açúcar
    Saída esperada:
        O item açúcar precisa ser comprado.
    """
    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    pantry: List[str] = [
        'chocolate branco',
        'chocolate negro',
        'bolacha',
        'café',
        'leite',
        'arroz integral',
        'óleo de soja',
        'bandeija de ovos',
        'margarina sem sal',
    ]
    search: str = input(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} Inform a product to search: ')

    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} search in pantry? {colored(search in pantry, 'green', attrs=CGATTRS)}')

    for product in pantry:
        if search.lower() == product.lower():
            print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} product founded {colored(search, 'blue', attrs=CGATTRS)} ')
            return

    print(f'{colored("[LISTS_TUPLES][01]", "white", attrs=CGATTRS)} Product not found: {colored(search, 'red', attrs=CGATTRS)} - {colored('you need buy it!', 'yellow', attrs=CGATTRS)}')


def exerc_02() -> None:
    """
    Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.
    Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.
    Exemplo de Entrada: Notas: [85, 70, 90, 60, 75] - Saída esperada: Notas ordenadas: [60, 70, 75, 85, 90]
    """
    print(f'{colored("[LISTS_TUPLES][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    grades: List[int] = [85, 70, 90, 60, 75]
    print(f'{colored("[LISTS_TUPLES][02]", "white", attrs=CGATTRS)} Grades original {colored(grades, "blue", attrs=CGATTRS)} :: Grades sorted {colored(sorted(grades), "red", attrs=CGATTRS)}')
    grades.sort()
    print(f'{colored("[LISTS_TUPLES][02]", "white", attrs=CGATTRS)} Grades sort in-place {colored(grades, "magenta", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
    Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.
    Exemplo de Entrada:
    Digite o nome do voluntário (ou 'sair' para encerrar): Ana
    Digite o nome do voluntário (ou 'sair' para encerrar): João
    Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
    Digite o nome do voluntário (ou 'sair' para encerrar): sair
    Saída esperada: Voluntários registrados: ['Ana', 'João', 'Mariana']
    """
    print(f'{colored("[LISTS_TUPLES][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    volunteers: List[str] = []
    while True:
        name: str = input('Inform the name of volunter: ')
        if name.lower() in ('exit', 'e', 'end', '', 'sair', 'salir'):
            print(f'{colored("[LISTS_TUPLES][03]", "white", attrs=CGATTRS)} Volunteers: {colored(volunteers, "red", attrs=CGATTRS)}')
            break

        volunteers.append(name)


def exerc_04() -> None:
    """
    Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
    Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?
    Exemplo de Entrada:
        Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
        Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar
    Saída esperada: Estoque combinado: ('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')
    """
    print(f'{colored("[LISTS_TUPLES][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    pantry_01: Tuple(str) = ('Arroz', 'Feijão', 'Macarrão')
    pantry_02: Tuple(str) = ('Óleo', 'Sal', 'Açúcar')
    pantry: Tuple(str) = pantry_01 + pantry_02
    print(f'{colored("[LISTS_TUPLES][04]", "white", attrs=CGATTRS)} Full pantry: {pantry}')


def exerc_05() -> None:
    """
    Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.
    Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?
    Exemplo de Entrada:
        Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
        Digite o nome do novo convidado: João
        Digite a posição na qual deseja inserir o convidado: 2
    Saída esperada: Lista atualizada de convidados: ['Ana', 'João', 'Pedro', 'Carlos']
    """
    print(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    guests: List[str] = []
    while True:
        guest: str = input(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} Inform guest name (exit to finish the program): ')
        if guest in ('exit', 'e', 'end', '', 'sair', 'salir'):
            break
        position: int = int(input(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} Inform the desired position (integer number between 0 - {len(guests) if len(guests) > 0 else 0}): '))
        if position < 0 or position > len(guests) or len(guests) == 0:
            position = 0
            print(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} Position will be DEFAULT: 0')

        guests.insert(position, guest)
        print(f'{colored("[LISTS_TUPLES][05]", "white", attrs=CGATTRS)} {colored(guests, "red", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante. Os eventos foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.
    Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    Saída esperada: Ordem corrigida: ['Abertura', 'Palestra 2', 'Palestra 3', 'Encerramento']
    """
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    events: List[str] = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} original {colored(events, "blue", attrs=CGATTRS)} :: NORMAL')
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} reversed {colored(list(reversed(events)), "red", attrs=CGATTRS)} :: list(reversed(events))')
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} reversed {colored(events[::-1], "yellow", attrs=CGATTRS)} :: events[::-1]')
    events.reverse()
    print(f'{colored("[LISTS_TUPLES][06]", "white", attrs=CGATTRS)} reversed {colored(events, "green", attrs=CGATTRS)} :: events.reverse()')


def exerc_07() -> None:
    """
    O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
    Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?
    Exemplo de Entrada: Digite o nome incorreto: Carlos Digite o nome correto: João
    Saída esperada: O nome Carlos foi substituído por João. Lista atualizada: ['Ana', 'João', 'Pedro']
    """
    print(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    participants: List[str] = ['Ana', 'João', 'Pedro', 'Lucas', 'José', 'Mário', 'Jorge', 'Maria', 'Marta', 'Otto', 'Júlia', 'Priscila', 'Emerson']
    correct: str = input(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} Inform the correct name: ')
    wrong: str = input(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} Inform the wrong name: ')
    print(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} original..: {colored(participants, "red", attrs=CGATTRS)}')
    for index, participant in enumerate(participants):
        if participant == wrong:
            participants[index] = correct
            break

    print(f'{colored("[LISTS_TUPLES][07]", "white", attrs=CGATTRS)} correct...: {colored(participants, "blue", attrs=CGATTRS)}')


def exerc_08() -> None:
    """
    Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.
    Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.
    Exemplo de Entrada: Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa
    Saída esperada: Pedidos finais: ['Sanduíche', 'Suco']
    """
    print(f'{colored("[LISTS_TUPLES][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    orders: List[str] = ['Sanduíche', 'Suco', 'Sobremesa', 'Proção Fritas', 'Refrigerante', 'Pastel']
    print(f'{colored("[LISTS_TUPLES][08]", "white", attrs=CGATTRS)} original..: {colored(orders, "red", attrs=CGATTRS)}')
    order_removed: str = orders.pop()
    print(f'{colored("[LISTS_TUPLES][08]", "white", attrs=CGATTRS)} after.....: {colored(orders, "yellow", attrs=CGATTRS)} :: removed {colored(order_removed, "blue", attrs=CGATTRS)}')


def exerc_09() -> None:
    """
    A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.
    Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.
    Exemplo de Entrada: Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8
    Saída esperada: Média final da turma: 7.88
    """
    print(f'{colored("[LISTS_TUPLES][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[LISTS_TUPLES][09]", "white", attrs=CGATTRS)} TODO implement!!')


def exerc_10() -> None:
    print(f'{colored("[LISTS_TUPLES][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[LISTS_TUPLES][10]", "white", attrs=CGATTRS)} TODO implement!!')
