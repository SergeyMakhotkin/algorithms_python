import string

letter_string = string.ascii_lowercase

while True:
    number = input("Введите порядковый номер буквы: \n")
    try:
        number = int(number)
        if 0 < number <= len(letter_string):
            break
        print("Вы ввели число, не входящее в пределы алфавита")
    except ValueError:
        print("Вы ввели некорректное значение")

letter_string = ' ' + letter_string
print(f"Номеру {number} соответствует буква ", letter_string[number])

