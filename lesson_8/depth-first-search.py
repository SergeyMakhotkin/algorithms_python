"""
Алгоритм обхода графа в глубину (задача: обойти все вершины)
1) вариант с определением графа через матрицу смежности
"""

graph = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
]

is_visited = [False] * len(graph)

def dfs_adj_matrix(graph, vertex, visited_list):
    visited_list[vertex] = True
    print(vertex)
    for next_vertex, weight in enumerate(graph[vertex]):
        if weight != 0:
            if not visited_list[next_vertex]:
                dfs_adj_matrix(graph, next_vertex, visited_list)


dfs_adj_matrix(graph, 0, is_visited)
