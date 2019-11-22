'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

'''

from hashlib import sha1


def substr_counter(str, verbose=0):
    str_length = len(str)
    hash_dict = set()
    # модуль системы счисления для входных данных, состоящих только из строчных латинских букв

    # изменение начального индекса подстроки
    for i in range(str_length):
        for substr_len in range(1, str_length):
            j = i
            while j + substr_len <= str_length:
                x = str[i:j + substr_len]
                hx = sha1(str[i:j + substr_len].encode('utf-8')).hexdigest()
                if hx not in hash_dict:
                    hash_dict.add(hx)
                    if verbose != 0:
                        print(x)
                j += 1

    # print(hash_dict)
    return len(hash_dict)


s = input("Введите строку символов: \n")
print(f'в введенной строке {substr_counter(s)} подстрок')
