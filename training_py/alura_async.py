import asyncio
import math
import time
from typing import List

from termcolor import colored


CGATTRS: List[str] = ['bold', ]


async def class02() -> None:
    async def coroutine(number: int) -> None:
        print(f'Running task {number}')
        await asyncio.sleep(number)
        print(f'Finished task {number}')

    async def coroutine_from_future(number: int, future: asyncio.Future) -> None:
        print(f'Start for number {number}')
        await asyncio.sleep(number)
        future.set_result(f'End for number {number}')

    # await asyncio.sleep(1)
    task_01 = asyncio.create_task(coroutine(number=1))
    task_02 = asyncio.create_task(coroutine(number=2))
    await task_01
    await task_02

    future_01 = asyncio.Future()
    asyncio.create_task(coroutine_from_future(number=1, future=future_01))
    result_01 = await future_01
    print(f'{result_01=}')

    print('Time sleep without async:')
    time.sleep(2)


async def exerc_01() -> None:
    """
    Alice é uma desenvolvedora que precisa testar uma API de terceiros que tem um tempo de resposta variável.
    Para simular esse comportamento, ela quer um programa que exiba uma mensagem, aguarde um tempo determinado e depois exiba outra mensagem informando que o tempo acabou.
    Esse programa deve ser assíncrono, permitindo que Alice compreenda melhor como funciona a espera sem bloquear a execução do código.
    Com base nesse cenário, crie um programa que aguarde 3 segundos antes de exibir a mensagem final.
    Saída esperada:
    > Iniciando temporizador...
    > Tempo finalizado após 3 segundos!
    """
    async def api(number: int) -> None:
        print(f'{colored("[ALURA_ASYNC][01]", "white", attrs=CGATTRS)} {colored("STARTING...:", "yellow", attrs=CGATTRS)} api {colored(number, "yellow", attrs=CGATTRS)}')
        await asyncio.sleep(number * 1.5)
        print(f'{colored("[ALURA_ASYNC][01]", "white", attrs=CGATTRS)} {colored("FINISHING..:", "red", attrs=CGATTRS)} api {colored(number, "red", attrs=CGATTRS)}')

    print(f'{colored("[ALURA_ASYNC][01]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    await asyncio.gather(api(number=3), api(number=1), api(number=2))


async def exerc_02() -> None:
    """
    Carlos é um engenheiro de software que precisa processar duas tarefas simultaneamente: uma que simula um download e outra que simula uma análise de dados. Ele quer que ambas as tarefas sejam iniciadas ao mesmo tempo, e que o programa exiba mensagens informando o início e o fim de cada uma.
    Com base nesse cenário, crie um programa que inicie ambas as tarefas ao mesmo tempo, e exiba as mensagens quando cada uma for concluída. Dica: Utilize asyncio.gather() para rodar ambas em paralelo.
    Saída esperada:
    > Iniciando download...
    > Iniciando análise de dados...
    > Download concluído!
    > Análise de dados concluída!
    """
    async def download() -> None:
        print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} {colored("START", "red", attrs=CGATTRS)} download...')
        await asyncio.sleep(3)
        print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} {colored("END", "red", attrs=CGATTRS)} download...')

    async def analysys() -> None:
        print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} {colored("START", "yellow", attrs=CGATTRS)} analysys...')
        await asyncio.sleep(5)
        print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} {colored("END", "yellow", attrs=CGATTRS)} analysys...')

    print(f'{colored("[ALURA_ASYNC][02]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    await asyncio.gather(download(), analysys())


async def exerc_03() -> None:
    """
    Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.
    Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.
    Dica: use a função sleep para simular um tempo de processamento.
    Dica: para testar o funcionamento do seu código, utilize uma lista de números em ordem de tamanho aleatória. Exemplo: numeros = [5, 3, 7, 4, 6]
    Saída esperada:
    > Fatorial de 3 = 6
    > Fatorial de 4 = 24
    > Fatorial de 5 = 120
    > Fatorial de 6 = 720
    > Fatorial de 7 = 5040
    """
    async def recursive_factorial(number: int, sl: int = 1) -> int:
        if number == 1:
            return 1

        sub = await recursive_factorial(number - 1)
        await asyncio.sleep(sl)

        return number * sub

    async def factorial(number: int) -> None:
        await asyncio.sleep(number)
        print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} Factorial for {colored(number, "blue", attrs=CGATTRS)} is {colored(math.factorial(number), "magenta", attrs=CGATTRS)}')

    print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    numbers: List[int] = [5, 3, 7, 4, 6]

    tasks = [asyncio.create_task(factorial(number=n)) for n in numbers]
    await asyncio.gather(*tasks)

    print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} --- RECURSIVE ---')
    recursive_tasks = [recursive_factorial(number=n, sl=n) for n in numbers]
    results: List[int] = await asyncio.gather(*recursive_tasks)
    for num, res in zip(numbers, results):
        print(f'{colored("[ALURA_ASYNC][03]", "white", attrs=CGATTRS)} Factorial for {colored(num, "cyan", attrs=CGATTRS)} is {colored(res, "yellow", attrs=CGATTRS)}')


async def exerc_04() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][04]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][04]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_05() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][05]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][05]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_06() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][06]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][06]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_07() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][07]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][07]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_08() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][08]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][08]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_09() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][09]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][09]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')


async def exerc_10() -> None:
    """
    TODO start it
    """
    print(f'{colored("[ALURA_ASYNC][10]", "white", attrs=CGATTRS)} --- EXERCISE ---')
    print(f'{colored("[ALURA_ASYNC][10]", "white", attrs=CGATTRS)} TODO {colored("implement it!!", "red", attrs=CGATTRS)}')
