import asyncio
import random
import time


async def coroutine_task(iteraction):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f"Iteracao {iteraction}, tempo decorrido: {process_time}")
    # Aqui nao poderiamos usar a funcao time.sleep(process_time)
    # porque a mesma eh bloqueante.


async def coroutine_task_01():
    # Aqui existe uma iteracao apenas para executar criar Tasks
    # chamado a funcao coroutine_task, que eh uma corrotina.
    tasks = []
    for iteraction in range(10):
        tasks.append(asyncio.create_task(coroutine_task(iteraction)))
    # As Task sao agrupadas em uma lista e passadas para o metodo
    # asyncio.gather, para que sejam executada concorrentemente.
    # O uso de await infoma ao loop um ponto de bloquei e que a
    # corrotina/tarefa podera ser suspensa para que o controle
    # seja passado para outra corrotina.
    # Outra observacao a ser feita eh que o asyncio.create_task pode
    # ser substituido tranquilamente pela funcao
    # asyncio.ensure_future. O exemplo com asyncio.ensure_future
    # eh demonstrado na couroutine coroutine_task_02
    await asyncio.gather(*tasks)


async def coroutine_task_02():
    # A coroutine_task_02 faz exetamente a mesma coisa que a
    # coroutine_task_01, a unica diferenca eh que neste exemplo
    # asyncio.gather nao eh utilizado.
    # O loop ira suspender o controle para as outras corrotinas
    # que estao fora deste contexto de execucao. Mas, as tarefas
    # desta coroutina nao irao ser executadas de forma concorrente.
    # A nao ser que voltemos a usa a funcao asyncio.gather ou
    # outra funcao que tenha funcionalidade semelhante.
    for iteraction in range(10):
        task = asyncio.ensure_future(coroutine_task(iteraction))
        await task
    # asyncio.gather(*tasks)
    # Descomente esta funcao para obter concorrencia.


def main():
    # Estrategias para inicializar o loop de execucao das
    # couroutines e Tasks. UTILIZE APENAS UMA das opcoes abaixo e
    # comente as demais.
    # -----------------------------------------------------------
    # 1. A funcao asyncio.run captura automaticamente o loop de
    # evento e quando todas as tarefas sao executadas a funcao
    # loop.close() eh chamada implicitamente.
    # Esta eh a opcao mais recomendada pela documentacao.
    # -----------------------------------------------------------
    asyncio.run(coroutine_task_01())
    # 2. run_until_complete - Mantem o loop em execucao ate que
    # todas as tasks sejam executadas. Apos isso o loop e a
    # aplicacao sao encerrados.
    # -----------------------------------------------------------
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(coroutine_task_01())
    # loop.close()
    # 3. Mantem o loop em execucao por tempo indefinido.
    # O loop so sera encerrado com Control+C ou se for
    # chamada a funcao loop.stop()
    # -----------------------------------------------------------
    # loop = asyncio.get_event_loop()
    # task_function = asyncio.ensure_future(coroutine_task_01())
    # loop.run_forever()


if __name__ == "__main__":
    main()
