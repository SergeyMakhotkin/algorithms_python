size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

def shell_sort(array):

    assert len(array) < 4000, "Массив слишком большой для данной сортировки"

      # генератор шага инкремента
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 705, 1750]
        while len(array) <= inc[-1]:
            inc.pop()  # получили список инкрементов, подходящий для переданного массива

        while len(array) > 0:
            yield
