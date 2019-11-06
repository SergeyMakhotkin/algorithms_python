import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

n = 1  # счетчик витков сортировки
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i+1], array[i]
    n += 1

print(array)
