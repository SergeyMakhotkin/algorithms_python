import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):
    for i in range(len(array)):
        idx_min = i  # переменная для промежуточного значения

        for j in range(i + 1, len(array)):  # проход по неотсортированной части массива
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)

selection_sort(array)
print('*'* 30, '\n', array)

# каждая итерация цикла увеличивает на 1 отсортированную часть слева
# и уменьшает на 1 неотсортированную часть справа