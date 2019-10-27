# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

random_range = 100
number = int(input("Сколько элементов должно быть в массиве? \n"))
arr = [random.randint(-random_range, random_range) for _ in range(number)]
print(arr)
min_item = random_range
min_position = None
max_item = -random_range
max_position = None
sum = 0
for i in range(number):
    if arr[i] > max_item:
        max_item = arr[i]
        max_position = i
    if arr[i] < min_item:
        min_item = arr[i]
        min_position = i

print(f'мин позиция: {min_position}, минимальный элемент: {min_item}')
print(f'макс позиция: {max_position}, максимальный элемент: {max_item}')
if abs(max_position - min_position):
    for i in range(min(min_position, max_position) + 1, max(min_position, max_position)):
        sum += arr[i]
    print(f"Сумма элементов между максимальным и минимальным элементами равна: {sum}")
else:
    print("Максимальный и минимальный элементы находятся рядом")
