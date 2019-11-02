from collections import Counter

# c = collections.Counter()
#     for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
#         c[word] += 1


a = Counter()
b = Counter('abracadabra')
c = Counter({'key_1': 1, 'key_2': 2, 'key_3': 3})
d = Counter(cat='asd', dog=20)

b['z'] = 0
b['y'] = 0
# print(c['key_1'])
# print(b)
print(list(b))  # вывод ключей, он же - список уникальных элементов
print(set(b))  # вывод ключей, он же - список уникальных элементов
# print(list(b.elements()))  # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# print(b.most_common(4))
# print(b.most_common()[:-4:-1])  # 3 наиболее редко встречающиеся элементы
# print(b)
# b += Counter()  # удалить элементы, встречающиеся менее 1 раза
# print(b)


g = Counter({'a': 1, 'b': 2, 'c': 4, 'd': 8})
f = Counter(a=2, b=23, c=-1)  # коллекция, основанная на ключевых аргументах
# print('old g:', g)
# print('old f:', f)
# f.subtract(g)
# print("New f:", f)

x = Counter(g=239, h=704, s=13, p=-49, t=-8)
z = Counter(g=178, h=25, s=39, u=-678, t=-666)
print(x)
print(z)
print('x + z = ', x + z)
print('x - z = ', x - z)
# x.subtract(z)
# print(x)
# print("x.substract(z): ", y)
print('x | z = ', x | z)  # объединение
print('x & z = ', x & z)  # пересечение

print('-x: ', -x)
print('+x: ', +x)
print('-z: ', -z)
print('+z: ', +z)
