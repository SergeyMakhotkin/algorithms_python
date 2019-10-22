while True:
    x = input("Введите год для проверки: \n")
    try:
        x = int(x)
        break
    except ValueError:
        print("Вы ввели некорректное значение")
if not(x % 4):
    if not (x % 100):
        if not (x % 400):
            print(f"Год {x} високосный")
        else:
            print(f'Год {x} не високосный')
    else:
        print(f'Год {x} високосный')
else:
    print(f"Год {x} не високосный")