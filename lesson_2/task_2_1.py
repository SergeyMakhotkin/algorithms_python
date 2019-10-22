# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.


action = ''
while action != '0':
    while True:
        a = input("Введите первое число: \n")
        try:
            a = float(a)
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова")

    while True:
        b = input("Введите второе число: \n")
        try:
            b = float(b)
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова")

    while True:
        action = input("Введите символ математической операции (+, -, *, /) "
                       "либо введете ноль для завершения программы: \n")
        if action == '0':
            break
        elif action == '+':
            print("Сумма равна: ", a + b)
            break
        elif action == '-':
            print("Разность равна: ", a - b)
            break
        elif action == '*':
            print("Произведение равно: ", a * b)
            break
        elif action == '/':
            if b == 0:
                print("Нельзя делить на 0!")
            else:
                print("Частное равно: ", a / b)
                break
        else:
            print("Вы ввели некоректное действие. Попробуйте снова")
print("До свидания!")
