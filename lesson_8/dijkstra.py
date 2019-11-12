'''
Алгоритм Дейкстры
Нахождение минимального пути ко всем вершинам графа.
(работает для графов с положительным весом ребер)

'''

from collections import deque

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 10],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    # для хранения информации о пройденных вершинах (пути)
    path = [[] for _ in range(length)]

    cost[start] = 0
    min_cost = 0  # показывает, двигаемся ли мы по графу
    while min_cost < float('inf'):
        is_visited[start] = True


        # вычисление стоимости пути до смежных вершин.
        # в цикле проверяем, есть ли ребра к вершинам, которые мы не посещали
        # если да - проверяем расстояния до них
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                # если новое расстояние до вершины меньше того, которое хранится в списке cost,
                # то заменить стоимость на новую
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    # записываем информацию о (новом) родителе

                    parent[i] = start
                    path[i].append(start)

        min_cost = float('inf')
        for i in range(length):
            # если стоимость маршрута в списке cost до вершины i больше, чем новая вычесленная, то меняем
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, path


if __name__ == '__main__':
    start = int(input("От какой вершины начинать поиск? "))
    print(dijkstra(graph, start))
