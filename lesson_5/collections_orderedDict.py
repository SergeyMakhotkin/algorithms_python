from collections import OrderedDict

a = {'z': 1, 'b': 7, 'h': 8, 'y': 53, 'a': 9, 'c': 92}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(a)
print(new_a)

# Методы
# elem = new_a.popitem(last=False)
# print(elem)
new_a['asdf'] = 234  # новый элемент в любом случае добавляется в конец отсортированного словаря
print(new_a)
new_a.move_to_end('a')
new_a.move_to_end('y', last=False)
print(new_a)
new_b = OrderedDict(sorted(new_a.items(), key=lambda x: x[1]))
print(new_b)

new_b['z']=385

print(new_b)  # При изменениии элемента в OrderedDict его порядок не изменяется


# Возможность сортировки по длинне ключа
new_c = OrderedDict(sorted(new_a.items(), key=lambda x: -len(x[0])))
print(new_c)

# reversed
print("*"*30)
print(new_b)
for key in reversed(new_b):
    print(key, new_b[key])
