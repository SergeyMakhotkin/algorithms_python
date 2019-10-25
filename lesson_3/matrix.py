import random


def print_matrix(matrix):
    question_1 = input("Напечатать сумму элементов строк? (введите Y/N): \n").lower()
    if question_1 == 'y' or question_1 == 'д':
        print_rowsum = True
    else:
        print_rowsum = False

    question_2 = input("Напечатать сумму элементов столбцов? (введите Y/N): \n").lower()
    if question_2 == 'y' or question_2 == 'д':
        print_columnsum = True
    else:
        print_columnsum = False

    columnsum = [0 for _ in range(len(matrix[0]))]

    for line in matrix:
        rowsum = 0
        for j, item in enumerate(line):
            rowsum += item
            columnsum[j] += item
            print(f'{item:>5}', end='')
        print(' ' * 4, '|', f'{rowsum:>3}') if print_rowsum else print()
    if print_columnsum:
        print('*'*len(matrix[0])*5)
        for csum in columnsum:
            print(f'{csum:>5}', end='')
        print()


rows = 5
columns = 8
matrix_1 = [[random.randint(0, 100) for _ in range(columns)] for _ in range(rows)]

print_matrix(matrix_1)

