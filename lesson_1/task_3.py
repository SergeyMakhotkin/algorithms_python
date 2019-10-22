# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
import string

int_range_a = False
int_range_b = False
float_range_a = False
float_range_b = False
while not (int_range_a):
    int_range_a = input("Введите начало диапазона целых чисел: ")
    try:
        int_range_a = int(int_range_a)
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте снова.")
        int_range_a = False

while not (int_range_b):
    int_range_b = input("Введите конец диапазона целых чисел: ")
    try:
        int_range_b = int(int_range_b)
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте снова.")
        int_range_b = False

print(f"Случайное число из диапазона от {int_range_a} до {int_range_b}: ", random.randint(int_range_a, int_range_b))

while not (float_range_a):
    float_range_a = input("Введите начало диапазона вещественных чисел: ")
    try:
        float_range_a = float(float_range_a)
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте снова.")
        float_range_a = False

while not (float_range_b):
    float_range_b = input("Введите конец диапазона целых чисел: ")
    try:
        float_range_b = float(float_range_b)
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте снова.")
        float_range_b = False

print(f"Случайное вещественное число из диапазона от {float_range_a} до {float_range_b}: ",
      random.random() * (float_range_b - float_range_a) + float_range_a)

letters = string.ascii_lowercase
while True:
    letters_range_a = input("Введите букву от 'a' до 'z': ").lower()
    if letters_range_a in letters:
        break
    print("Вы ввели символ не входящий в диапазон 'a - z'.")

while True:
    letters_range_b = input("Введите букву от 'a' до 'z': ").lower()
    if letters_range_b in letters:
        break
    print("Вы ввели символ не входящий в диапазон 'a - z'.")

print(f"Случайный символ из диапазона от {letters_range_a} до {letters_range_b}: ",
      letters[random.randint(0, len(letters) - 1)])
