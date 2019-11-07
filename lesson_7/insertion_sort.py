import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(f"{str(array):>72}")


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
            print(f"результат промежуточного цикла: {str(array):>40}")
        array[j] = spam
        print(f"внешний цикл: {str(array):>58}")


insertion_sort(array)
print(f"{str(array):>72}")
