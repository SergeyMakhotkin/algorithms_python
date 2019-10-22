# print("Расчет НОД по алгоритму Евклида (вычитание) \n", '#'*15)
# a = int(input("введите 1 число: \n"))
# b = int(input("введите 2 число: \n"))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)


print('Алгоритм Евклида с использованием рекурсивной функции')
a = int(input('Введите значение первого числа: \n'))
b = int(input('Введите значение второго числа: \n'))


# def gcd(x, y):
#     if y == 0:
#         return x
#     return gcd(y, x % y)
#
#

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

print(gcd(a, b))
