# Поиск подстроки в строке с использованием технологии хэширования
# Алгоритм Рабина-Карпа

import hashlib


def Rabi_Karp(s: str, subs: str):
    assert len(s) > 0 and len(subs) > 0, "Строки не могут быть пустыми"
    assert len(subs) <= len(subs), "Подстрока длиннее строки"

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            # дополнительная проверка если хэши совпадут
            if s[i:i + len_sub] == subs:  # если строки длинные, то проверка займет большое время
                return i
    return -1


s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку для поиска: ')

pos = Rabi_Karp(s_1, s_2)
print(f'Подстрока найдена в позиции {pos}' if pos != -1 else 'Подстрока не найдена')
