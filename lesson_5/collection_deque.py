# свойства:
# 1) самоорганизация;
# 2) произвольное расположение элементов.
# время доступа к первому и последнему элементу очереди равно константе
# время доступа к n-элементу очереди зависит от (размера очереди)


from collections import deque

# очередь основана на списке
# для создания очереди, внутрь нужно передать итерируемый объект

a = deque()
b = deque('sajdfl')
z = 1, 2, 3, 4, 5
# print(type(z))
c = deque(z, maxlen=2)
print(type(c))
# c = deque(1, 2, 3, 4)  такой вариант передачи кортежа не работает
d = deque(['a', 'b', 'c'])

print(a, b, c, d, sep='\n')
b.clear()

# добавление элементов в очередь
b = deque((el for el in range(0, 5)), maxlen=8)
print(b)
b.append('a')
b.appendleft('z')
print(b)
b.extend(d)
print(b)
b.extend((1, 2, 3, 4))
print(b)
b.extendleft([1, 2, 3])
print(b)
x = b.pop()
y = b.popleft()
print(x, y, b, sep='\n')

print(b.count('a'))
print(b.index(1))
b.insert(3, 'z')
print(b)
b.reverse()
print("reversed b: ", b)
b.extendleft([-4, -6, -7])
print(b)
b.rotate(3)
print(b)
