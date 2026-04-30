from typing import Any, Dict, List, Set, Tuple

from termcolor import colored


CGATTRS: List[str] = ['bold', ]
STOP_KEYWORDS: Tuple[str] = ('exit', 'bye', 'end', 'quit', 'salir', 'sair', 'adios', '')


def exerc_01() -> None:
    """
    Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.
    Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.
    Exemplo de entrada:
    > Digite o nome do convidado: Ana
    > Digite o nome do convidado: João
    > Digite o nome do convidado: Ana
    > Digite o nome do convidado: Carla
    > Digite o nome do convidado: sair
    Saída esperada: Convidados confirmados: Ana, João, Carla
    """
    print(f'{colored("[SETS_DICTS][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    guests: Set = set()
    while True:
        guest: str = input("Inform the guest's name: ")
        if guest.lower() in STOP_KEYWORDS:
            print(f'{colored("[SETS_DICTS][01]", "white", attrs=CGATTRS)} guests: {colored(guests, "red", attrs=CGATTRS)}')
            break

        guests.add(guest)


def exerc_02() -> None:
    """
    Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
    Exemplo de entrada:
    > Texto 1: O sol brilha forte no céu azul
    > Texto 2: O céu azul anuncia um dia de sol intenso
    Saída esperada: Palavras em comum: {'o', 'azul', 'sol', 'céu'}
    """
    texts: List[str] = [
        'O sol brilha forte no céu azul',
        'O céu azul anuncia um dia de sol intenso'
    ]
    print(f'{colored("[SETS_DICTS][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    text_01: Set = set(texts[0].lower().split(' '))
    text_02: Set = set(texts[1].lower().split(' '))
    print(f'{colored("[SETS_DICTS][02]", "white", attrs=CGATTRS)} {colored(text_01.intersection(text_02), "red", attrs=CGATTRS)}')


def exerc_03() -> None:
    """
    Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
    - Quais itens apareceram nas duas listas
    - Quais foram exclusivos de Laura
    - Quais foram exclusivos da Ana
    Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
    Exemplo de entrada:
    > Lista de Laura: leite, pão, café, açúcar
    > Lista de Ana: pão, café, biscoito, chocolate
    Saída esperada:
    > Itens em ambas as listas: pão, café
    > Itens exclusivos de Laura: leite, açúcar
    > Itens exclusivos de Ana: biscoito, chocolate
    """
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    shopping_list_01: Set = set(['leite', 'pão', 'café', 'açúcar'])
    shopping_list_02: Set = set(['pão', 'café', 'biscoito', 'chocolate'])
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} shopping list 01............: {colored(shopping_list_01, "red", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} shopping list 02............: {colored(shopping_list_02, "yellow", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items in all lists..........: {colored(shopping_list_01.intersection(shopping_list_02), "magenta", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items exclusive in list 01..: {colored(shopping_list_01.difference(shopping_list_02), "blue", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][03]", "white", attrs=CGATTRS)} items exclusive in list 02..: {colored(shopping_list_02.difference(shopping_list_01), "cyan", attrs=CGATTRS)}')


def exerc_04() -> None:
    """
    Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.
    Exemplo de entrada:
    > CASO 01:
    Permissões principais: leitura, escrita, execução, compartilhamento
    Permissões solicitadas: leitura, escrita
    > CASO 02:
    Permissões principais: leitura, escrita, execução, compartilhamento
    Permissões solicitadas: leitura, exclusão
    Saída esperada:
    > CASO 01:
    As permissões solicitadas fazem parte das permissões principais.
    > CASO 02:
    As permissões solicitadas não fazem parte das permissões principais.
    """
    print(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    main_permissions: Set(str) = set(['leitura', 'escrita', 'execução', 'compartilhamento'])
    granted_permissions: List[Set[str]] = [
        set(['leitura', 'escrita']),
        set(['leitura', 'exclusão'])
    ]
    while True:
        permissions: Set[str] = set(p.strip() for p in input(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} Inform a list of permissions separated by {colored(";", "cyan", attrs=CGATTRS)} : ').lower().split(';'))
        if any([p in STOP_KEYWORDS for p in permissions]):
            break
        granted_permissions.append(permissions)

    print(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} main permissions: {colored(main_permissions, "yellow", attrs=CGATTRS)}')
    for granted in granted_permissions:
        print(f'{colored("[SETS_DICTS][04]", "white", attrs=CGATTRS)} is subset? {colored(granted.issubset(main_permissions), "red", attrs=CGATTRS)} granted: {colored(granted, "magenta", attrs=CGATTRS)}')


def exerc_05() -> None:
    """
    Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.
    Exemplo de entrada:
    > equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
    > equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
    Saída esperada: Tarefas finais: {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'}
    """
    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    team_a: Set[str] = {"planejar reunião", "revisar documento", "testar sistema"}
    team_b: Set[str] = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
    joined: Set[str] = team_a.union(team_b)
    task_to_be_removed: str = input('Inform the task to be removed: ').lower()

    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} team_a: {colored(team_a, "red", attrs=CGATTRS)} team_b: {colored(team_b, "yellow", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} joined: {colored(joined, "blue", attrs=CGATTRS)}')
    joined.discard(task_to_be_removed)
    print(f'{colored("[SETS_DICTS][05]", "white", attrs=CGATTRS)} result: {colored(joined, "magenta", attrs=CGATTRS)}')


def exerc_06() -> None:
    """
    Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.
    Exemplo de entrada:
    > Digite o nome do produto: Caneta
    > Digite a quantidade: 50
    > Digite o nome do produto: Caderno
    > Digite a quantidade: 30
    > Digite o nome do produto: Borracha
    > Digite a quantidade: 20
    Saída esperada:
    Dicionário de produtos: {'Caneta': 50, 'Caderno': 30, 'Borracha': 20}
    """
    print(f'{colored("[SETS_DICTS][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    products: Dict[str, int] = {}
    while True:
        name: str = input(f"{colored('[SETS_DICTS][06]', 'white', attrs=CGATTRS)} Inform the product's name: ")
        if name in STOP_KEYWORDS:
            break

        quantity: int = int(input(f"{colored('[SETS_DICTS][06]', 'white', attrs=CGATTRS)} Inform the product's quantity: "))
        print(f'{colored("[SETS_DICTS][06]", "white", attrs=CGATTRS)} ----------')
        products[name] = quantity

    print(f'{colored("[SETS_DICTS][06]", "white", attrs=CGATTRS)} products: {colored(products, "red", attrs=CGATTRS)}')


def exerc_07() -> None:
    """
    Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.
    Exemplo de entrada:
    estoque = {"Caderno universitário": 50, "Caneta azul": 120, "Borracha branca": 30}
    > Nome do produto a ser atualizado: Caneta azul
    > Nova quantidade: 150
    Saída esperada: { "Caderno universitário": 50, "Caneta azul": 150, "Borracha branca": 30 }
    """
    print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    products: Dict[str, int] = {"Caderno universitário": 50, "Caneta azul": 120, "Borracha branca": 30}
    print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} products: {colored(products, "red", attrs=CGATTRS)}')
    name: str = input(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} Inform the product to be update: ')
    quantity: int = int(input(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} Inform the product to be update: '))
    if name in products:
        products[name] = quantity
        print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} products: {colored(products, "magenta", attrs=CGATTRS)}')
    else:
        print(f'{colored("[SETS_DICTS][07]", "white", attrs=CGATTRS)} product {colored(name, "magenta", attrs=CGATTRS)} not found!')


def exerc_08() -> None:
    """
    Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. Agora, ele precisa de um programa que apresente três informações:
    - Os nomes de todos os participantes.
    - As idades de todos os participantes.
    - Uma relação completa com o nome e a idade de cada um.
    Sua tarefa é criar esse programa com base nas informações fornecidas.
    Exemplo de entrada: participantes = {"Mariana": 25, "Carlos": 32, "Beatriz": 28, "Rafael": 35}
    Saída esperada:
    > Nomes dos participantes: Mariana, Carlos, Beatriz, Rafael
    > Idades dos participantes: 25, 32, 28, 35
    > Participantes e suas idades:
    - Mariana: 25 anos
    - Carlos: 32 anos
    - Beatriz: 28 anos
    - Rafael: 35 anos
    """
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    athletes: Dict[str, int] = {"Mariana": 25, "Carlos": 32, "Beatriz": 28, "Rafael": 35}
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} athletes..: {colored(athletes, "cyan", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} names.....: {colored(list(athletes.keys()), "magenta", attrs=CGATTRS)}')
    print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} ages......: {colored(list(athletes.values()), "red", attrs=CGATTRS)}')
    for name, age in athletes.items():
        print(f'{colored("[SETS_DICTS][08]", "white", attrs=CGATTRS)} each..: {colored(f"{name:<7}", "yellow", attrs=CGATTRS)} age..: {colored(age, "blue", attrs=CGATTRS)} ')


def exerc_09() -> None:
    """
    Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.
    Exemplo de entrada: participantes = {"Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, "Workshop 2": {"Fernanda", "Gustavo", "Helena"}}
    > Nome do participante a ser removido: Carla
    Saída esperada:
    > Lista atualizada de participantes:
    - Workshop 1: {'Alice', 'Bruno', 'Diego'}
    - Workshop 2: {'Fernanda', 'Gustavo', 'Helena'}
    """
    print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    attendees: Dict[str, Set[str]] = dict({"Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, "Workshop 2": {"Fernanda", "Gustavo", "Helena"}})
    print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} attendees: {colored(attendees, "blue", attrs=CGATTRS)}')
    name: str = input(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} Inform the name of attendee that will be removed: ')
    for key, values in attendees.items():
        if name in values:
            attendees[key].discard(name)
            print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} removed: {colored(name, "yellow", attrs=CGATTRS)}')
            break

    print(f'{colored("[SETS_DICTS][09]", "white", attrs=CGATTRS)} attendees: {colored(attendees, "red", attrs=CGATTRS)}')


def exerc_10() -> None:
    """
    Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.
    Exemplo de entrada:
    vendas = {
        "Eletrônicos": [
            {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000},
            {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500}
        ],
        "Eletrodomésticos": [
            {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000},
            {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800}
        ],
        "Livros": [
            {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50},
            {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100}
        ]
    }
    Saída esperada:
    > Total de vendas por categoria: 
    - Eletrônicos: R$ 14500.00 
    - Eletrodomésticos: R$ 9200.00 
    - Livros: R$ 1000.00 
    """
    print(f'{colored("[SETS_DICTS][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    sales: Dict[str, List[Dict[str, Any]]] = {
        "home_eletronics": [
            {"product": "Smartphone", "quantity": 5, "unit_value": 2000.00},
            {"product": "Tablet", "quantity": 3, "unit_value": 1500.00}
        ],
        "household_appliances": [
            {"product": "Geladeira", "quantity": 2, "unit_value": 3000.00},
            {"product": "Micro-ondas", "quantity": 4, "unit_value": 800.00}
        ],
        "books": [
            {"product": "Livro A", "quantity": 10, "unit_value": 50.00},
            {"product": "Livro B", "quantity": 5, "unit_value": 100.00}
        ]
    }

    resume: Dict[str, float] = dict()
    for category, sales_by_category in sales.items():
        total: float = 0.00
        for product in sales_by_category:
            total += int(product['quantity']) * float(product['unit_value'])
        resume[category] = total

    print(f'{colored("[SETS_DICTS][10]", "white", attrs=CGATTRS)} resume: {colored(resume, "red", attrs=CGATTRS)}')
