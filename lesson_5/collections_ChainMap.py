from collections import ChainMap

a = {'a': 2, 'b': 5, 'asd': 54}
b = {'a': 10, 'b': 59, 'zx': 25}

c_map = ChainMap(a, b)
print(c_map)

print(c_map['asd'])
print(c_map['zx'])
print(c_map['a'])

# методы
# .new_child() - добваление пустого словаря в начало
# .maps[]
print(c_map.maps[0])
print(c_map.maps[-1])

# .parents - возвращает ChainMap до домавления new_child
print('#'*30)
print(list(c_map))  # вывод всех ключей
print(list(c_map.values()))  # вывод всех значений