# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

random_range = 10
# number = int(input("Сколько элементов должно быть в массиве? \n"))
number = 20
arr = [random.randint(0, random_range) for _ in range(number)]
print(arr)
min_item_positions = [0]
for i in range(number):
    if arr[i] <= arr[min_item_positions[-1]]:
        min_item_positions.append(i)
print(f"Два минимальных элемента массива: {arr[min_item_positions[-1]]}, {arr[min_item_positions[-2]]}")

