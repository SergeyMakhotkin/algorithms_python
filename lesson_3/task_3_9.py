# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

column_number = int(input("Введите количество столбцов: \n"))
row_number = int(input("Введите количество строк: \n"))
random_min = -100
random_max = 100
min_items_in_column = [random_max for _ in range(column_number)]
max_of_min = random_min


matrix = [[random.randint(random_min, random_max) for _ in range(column_number)] for _ in range(row_number)]

print("Полученная матрица: \n")
for line in matrix:
    for item in line:
        print(f'{item:<7}', end='')
    print()


for i in range(row_number):
    for j in range(column_number):
        if matrix[i][j] < min_items_in_column[j]:
            min_items_in_column[j] = matrix[i][j]
print('*'*7*row_number+'\n', min_items_in_column)

for item in min_items_in_column:
    if item > max_of_min:
        max_of_min = item
print(f"максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min}")
