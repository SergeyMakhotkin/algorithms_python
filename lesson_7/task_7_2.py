# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 50
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def merge_sort(array):
    def merge(left, right):
        result = []
        i, j = 0, 0

        while i < len((left)) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        return result + left[i:] + right[j:]

    if len(array) < 2:
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    # print(left, right)
    return merge(left, right)


print(merge_sort(array))
