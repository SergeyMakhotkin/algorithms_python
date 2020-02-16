"""Функция для реализации бинарного поиска"""

import random


def bin_search(arr, value):
    """
    Функция принимает на вход массив данных и элемент, который нужно найти.
    Возвращает позицию элемента в массиве.
    :param arr:
    :param value:
    :return:
    """

    left_border_ind = 0
    right_border_ind = len(arr) - 1
    position_ind = len(arr) // 2

    while arr[position_ind] != value and left_border_ind <= right_border_ind:
        if value > arr[position_ind]:
            left_border_ind = position_ind + 1
        else:
            right_border_ind = position_ind - 1

        position_ind = (left_border_ind + right_border_ind) // 2

    return -1 if left_border_ind > right_border_ind else position_ind


test_arr = [random.randint(0, 1000) for _ in range(100)]
test_arr.sort()
print(f"Сгенерирован массив {test_arr}")
print('=' * 20)

search_value = int(input("Введите значение элемента для поиска: "))

result = bin_search(test_arr, search_value)
if result == -1:
    print("Элемент не найден.")
else:
    print(result)
