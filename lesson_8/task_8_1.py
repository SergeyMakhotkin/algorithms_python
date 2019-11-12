'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''



# 1) генерация графа

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

