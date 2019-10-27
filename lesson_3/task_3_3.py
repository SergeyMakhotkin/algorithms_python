# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

n = int(input("Введите количество элементов в массиве: \n"))
arr = []
min = 1000
max = 0
min_index = 0
max_index = 0
for i in range(n):
    item = random.randint(0, 1000)
    arr.append(item)
    if item < min:
        min = item
        min_index = i
    if item > max:
        max = item
        max_index = i
print("Был сгенерирован массив: ", arr)
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(f"{'Новый массив: ':>25}", arr, '\n',
      f"индекс максимального элемента: {max_index}", '\n',
      f"инедекс мимнимального элемента: {min_index}", '\n')
