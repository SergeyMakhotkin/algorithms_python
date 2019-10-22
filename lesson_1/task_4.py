import string

letter_string = string.ascii_lowercase
while True:
    letter_1 = input("Введите букву из диапазона 'a - z' :").lower()
    if letter_1 in letter_string:
        break
    print("Вы ввели некорректный символ")

while True:
    letter_2 = input("Введите еще одну букву из диапазона 'a - z' :").lower()
    if letter_1 in letter_string:
        break
    print("Вы ввели некорректный символ")

letter_string = ' ' + letter_string
number_letter_1 = letter_string.find(letter_1)
number_letter_2 = letter_string.find(letter_2)

print(f"Порядковый номер буквы {letter_1} :", number_letter_1)
print(f"Порядковый номер буквы {letter_2} :", number_letter_2)
print(f"В алфавите между буквой {letter_1} и буквой {letter_2} находится ",
      abs(number_letter_2 - number_letter_1 - 1), "букв(ы)")
