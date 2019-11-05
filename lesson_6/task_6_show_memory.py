import sys

memory_counter = []


def show_memory(*args, memory_counter=memory_counter, depth=1, level=0):
    global memory_counter = []
    if depth > 0:  # переменная depth регулирует уровень вложенности выполнения функции для итереируемых объектов
        depth -= 1
        for item in args:
            print('\t' * level, f"'Значение '{item}', тип данных {type(item)}, "
                                f"размер занимаемой памяти {sys.getsizeof(item)}'")

            memory_counter.append(sys.getsizeof(item))

            if hasattr(item, '__iter__'):
                if hasattr(item, 'items'):
                    for i in item.items():
                        show_memory(i, depth=depth, level=level + 2)
                elif not isinstance(item, str):
                    for i in item:
                        show_memory(i, depth=depth, level=level + 2)

    else:
        return sum(memory_counter)

if __name__ == "__main__":
    a = 12
    b = 'dsf'
    c = (23, 'sfgdsfdsfs')
    d = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}
    e = [a, b, c, d]

    print(show_memory(a, b, c, d, e))
    print(memory_counter)
