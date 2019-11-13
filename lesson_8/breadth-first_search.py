'''
Алгоритм поиска кратчайшего пути от одной вершины до другой(поиск в ширину)
для невзвешенного графа

1) Поместить вершину, с которой начинается поиск, в пустую очередь.
2) Извлечь из начала очереди вершину.
    a. Если вершина является целевой, завершить поиск.
    b. Иначе, в конец очереди поместить все смежные вершины, которые еще не были пройдены и не находятся в очереди.
3) Если очередь пуста, то все вершины графа были просмотрены. Следовательно, целевой узел недостижим из начального.
завершить поиск.

Дан неориентированный, невешенный граф.
'''

from collections import deque

graph = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],

]

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)
    return  f'Кратчайший путь {list(way)} длинной {cost} условных единиц'

s = int(input('Введите начальную вершину: '))
f = int(input('Введите конечную вершину: '))
print(bfs(graph, s, f))



