# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

column_number = 5
row_number = 4


def get_item(i, j):
    while True:
        elem = input(f"Введите {j + 1}-й элемент {i + 1}-й строки: \n")
        try:
            elem = int(elem)
            break
        except:
            ValueError
        print("Ошибка. Нужно вводить только целые числа")
    return (elem)


matrix = [[None for _ in range(column_number)] for _ in range(row_number)]
for i in range(row_number):
    line_sum = 0
    for j in range(column_number - 1):
        matrix[i][j] = get_item(i, j)
        line_sum += matrix[i][j]
    matrix[i][-1] = line_sum

print("Полученная матрица: \n")
for line in matrix:
    for item in line:
        print(f'{item:<7}', end='')
    print()
