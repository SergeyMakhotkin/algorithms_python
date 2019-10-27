# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

random_range = 100
N = int(input("Сколько элементов должно быть в массиве? \n"))
arr = [random.randint(-random_range, random_range) for _ in range(N)]
print(arr)
result_position = None
result_item = -random_range
i = 0
while i < N:
    if arr[i] < 0 and arr[i] > result_item:
        result_item = arr[i]
        result_position = i
    i += 1
print("В массиве нет отрицительных элементов") if result_position == None else print(
    "Максимальный отрицательный элемент "
    f"{result_item} с индексом {result_position}")
