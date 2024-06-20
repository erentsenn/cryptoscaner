import multiprocessing

from okx_module.okx_main import make_tickers_okx
from mexs_module.mexx_main import get_tickers_mexs
from bybit_module.bybit_main import make_orderbook_bybit
import timeit
import time
import datetime

def pair_search(graph, start):
    distance = {v: float('inf') for v in graph}
    predecessor = {v: None for v in graph}
    distance[start] = 0

    # Расслабление рёбер V-1 раз
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    # Проверка наличия циклов с отрицательным весом
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                # Наличие цикла, восстановление пути
                cycle = []
                current = v
                while True:
                    cycle.append(current)
                    current = predecessor[current]
                    if current in cycle:
                        cycle.append(current)
                        cycle = cycle[cycle.index(current):]
                        return cycle
    return None  # Цикл не найден

def worker_function(func):
    try:
        result = func()
        return result
    except Exception as e:
        return str(e)


def execute_and_send():
    functions = [make_orderbook_bybit, get_tickers_mexs, make_tickers_okx]
    with multiprocessing.Pool(processes=len(functions)) as pool:
        results = pool.map(worker_function, functions)
    return results


if __name__ == '__main__':
    graph = execute_and_send()
    print(graph[0])
    """
    for currency in graph:
        cycle = pair_search(graph, currency)
        if cycle:
            print(f"Арбитражный цикл найден: {' -> '.join(cycle)}")
            break
    else:
        print("Арбитражных циклов не найдено")
    """