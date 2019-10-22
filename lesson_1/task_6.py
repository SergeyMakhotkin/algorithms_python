# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

while True:
    a = input("Введите длину первого отрезка: \n")
    try:
        a = float(a)
        break
    except ValueError:
        print("Вы ввели некорректные данные")

while True:
    b = input("Введите длину второго отрезка: \n")
    try:
        b = float(b)
        break
    except ValueError:
        print("Вы ввели некорректные данные")

while True:
    c = input("Введите длину третьего отрезка: \n")
    try:
        c = float(c)
        break
    except ValueError:
        print("Вы ввели некорректные данные")

if (a >= b + c):
    print("Такого треугольника существовать не может")
elif (b >= a + c):
    print("Такого треугольника существовать не может")
elif (c >= a + b):
    print("Такого треугольника существовать не может")
else:
    if (a == b or b == c or c == a):
        if a == b == c:
            print("Треугольник равносторонний")
        else:
            print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
