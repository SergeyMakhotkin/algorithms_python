import sys


def show_memory(level, *args, ):
    for item in args:
        print('\t' * level, f"'Значение '{item}', тип данных {type(item)}, "
                            f"размер занимаемой памяти {sys.getsizeof(item)}'")
        if hasattr(item, '__iter__'):
            if hasattr(item, 'items'):
                for i in item.items():
                    show_memory(level + 2, i)
            elif not isinstance(item, str):
                for i in item:
                    show_memory(level + 2, i)


if __name__ == "__main__":
    a = 12
    b = 'dsf'
    c = (23, 'sfgdsfdsfs')
    d = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}
    e = [a, b, c, d]

    show_memory(0, a, b, c, d, e)
