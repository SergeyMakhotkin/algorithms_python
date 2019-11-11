import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
array_1 = array[:]
print(array_1)


def shell_sort(array):
    assert len(array) < 4000, "Массив слишком большой для данной сортировки"

    # генератор шага инкремента
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 705, 1750]
        while len(array) <= inc[-1]:
            inc.pop()  # получили список инкрементов, подходящий для переданного массива

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        changes_count = 0
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                else:
                    array[j - increment], array[j] = array[j], array[j - increment]
                    changes_count += 1
                    print(f"результат промежуточного цикла: {str(array):>10}")
        print(f"внешний цикл: {str(array):>20}")


    return changes_count


# print(shell_sort(array))
# print(array)

def shell_sort_1(array):
    assert len(array) < 4000, "Массив слишком большой для данной сортировки"

    # генератор шага инкремента
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 705, 1750]
        while len(array) <= inc[-1]:
            inc.pop()  # получили список инкрементов, подходящий для переданного массива

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        changes_count = 0
        for i in range(increment, len(array)):
            j = i
            spam = array[j]
            while array[j - increment] > spam and j >= increment:
                array[j] = array[j - increment]
                j -= increment
                changes_count +=1
                print(f"результат промежуточного цикла: {str(array):>10}")
            array[j] = spam
            print(f"внешний цикл: {str(array):>20}")

    return changes_count


print(shell_sort(array))
print(shell_sort_1(array_1))
print(array)
print(array_1)

