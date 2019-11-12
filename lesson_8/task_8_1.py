'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''


# 1) функция генерации графа

def get_graph(N):
    matrix = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 0
    return matrix


while True:
    N = input("Введите количество друзей: ")
    try:
        N = int(N)
        break
    except ValueError:
        print('Недопустимое значение')

graph_1 = get_graph(N)
print("Матрица смежности имеет вид:")
for i in graph_1:
    print(i)


def get_edge_count(graph):
    edges_set = set()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == graph_1[j][i] == 1:
                a = tuple(sorted([i, j]))
                edges_set.add(a)
    return len(edges_set)


print("Количество рукопожатий равно: ", get_edge_count(graph_1))

