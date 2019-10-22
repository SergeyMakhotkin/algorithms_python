while True:

    while True:
        a = input("Введите первое число: \n")
        try:
            a = float(a)
            break
        except ValueError:
            print("Вы ввели некорректное значение")

    while True:
        b = input("Введите второе число: \n")
        try:
            b = float(b)
            break
        except ValueError:
            print("Вы ввели некорректное значение")

    while True:
        c = input("Введите третье число: \n")
        try:
            c = float(c)
            break
        except ValueError:
            print("Вы ввели некорректное значение")

    if a != b or b != c or a != c:
        break
    else:
        print("Некорректный ввод. \nЧисла должны быть разными.")

if b > a > c or b < a < c:
    print(f"Из чисел {a}, {b} и {c} cредним является число {a}")
elif a > b > c or a < b < c:
    print(f"Из чисел {a}, {b} и {c} cредним является число {b}")
else:
    print(f"Из чисел {a}, {b} и {c} cредним является число {c}")
