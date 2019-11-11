import random


def median_search(array):
    def quick_select(array, k):
        # k - индекс элемента
        if len(array) == 1:
            return array[0]

        pivot = random.choice(array)
        less = [elem for elem in array if elem < pivot]
        great = [elem for elem in array if elem > pivot]
        eq = [elem for elem in array if elem == pivot]

        if k < len(less):
            return quick_select(less, k)
        elif k < len(less) + len(eq):
            return pivot
        else:
            return quick_select(great, k - len(less) - len(eq))

    if len(array) % 2 != 0:
        return quick_select(array, len(array) / 2)
    else:
        return 0.5 * (quick_select(array, len(array) / 2 - 1) + quick_select(array, len(array) / 2))


ar = [random.randint(0, 10) for i in range(10)]
print(ar)
print(median_search(ar))
print(sorted(ar))
