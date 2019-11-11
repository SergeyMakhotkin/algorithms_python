# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


import random

size = 10
array = [i for i in range(-size, size)]
random.shuffle(array)
print(array)



def bubble_sort_reverse(array):
    # при разделении массива на два отдельных с положительными и отрицательными элементами
    # количество операций сравнения уменьшается в 2 раза, при этом требуется доп. память
    count = 0
    positive = []
    negative = []
    for item in array:
        if item < 0:
            negative.append(item)
        else:
            positive.append(item)
    print(negative)
    print(positive)

    for i in range(len(positive)):
        for j in range(len(positive) - 1, i, -1):
            if positive[j - 1] < positive[j]:
                positive[j - 1], positive[j] = positive[j], positive[j - 1]
                count += 1

    for i in range(len(negative)):
        for j in range(len(negative) - 1, i, -1):
            if negative[j - 1] < negative[j]:
                negative[j - 1], negative[j] = negative[j], negative[j - 1]
                count += 1
    print("count = ", count)
    return positive + negative



print(bubble_sort_reverse(array))
print("=" * 30)

