import sys


def show_memory(*args, depth=1, level=0):
    if depth > 0:  # переменная depth регулирует уровень вложенности выполнения функции для итереируемых объектов
        depth -= 1
        for item in args:
            print('\t' * level, f"'Значение '{item}', тип данных {type(item)}, "
                                f"размер занимаемой памяти {sys.getsizeof(item)}'")

            if hasattr(item, '__iter__'):
                if hasattr(item, 'items'):
                    for i in item.items():
                        show_memory(i, depth=depth, level=level + 2)
                elif not isinstance(item, str):
                    for i in item:
                        show_memory(i, depth=depth, level=level + 2)





if __name__ == "__main__":
    a = 12
    b = 'dsf'
    c = (23, 'sfgdsfdsfs')
    d = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}
    e = [a, b, c, d]

    show_memory(a, b, c, d, e)
