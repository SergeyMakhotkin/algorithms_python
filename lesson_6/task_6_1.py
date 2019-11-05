# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо
# сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_6_task_1, les_6_task_2, и т.д.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
#
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
# с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.


# 1) Анализ памяти для программы из урока 5

from collections import defaultdict, OrderedDict
import sys

# импортируем модуль с функцией отображения размера занимаемой памяти
from lesson_6.task_6_show_memory import show_memory

while True:
    companies_number = input("Введите количество предприятий: \n")
    try:
        companies_number = int(companies_number)
        if companies_number > 0:
            break
    except ValueError:
        print("Неправильный ввод. Количество должно быть целым положительным числом")
companies = defaultdict(list)  # создаем defaultdict в котором будет храниться информация о предприятиях

for company in range(companies_number):  # заполняем словарь
    name = input(f"Введите название {company + 1}-компании: \n")  # цикл по предприятиям
    for i in range(4):  # цикл по кварталам
        while True:
            margin = input(f"Введите прибыль компании '{name}' за {i + 1}-й квартал : \n")
            try:
                margin = float(margin)
                break
            except ValueError:
                print("Недопустимое значение")

        companies[name].append(margin)
# print(companies)

all_av_margin = 0
for name, company_margin in companies.items():  # определяем среднюю годовую прибыль для каждого предприятия
    avarege_margin = sum(company_margin) / 4
    all_av_margin += avarege_margin
    companies[name].append(avarege_margin)

sorted_companies = OrderedDict(sorted(companies.items(), key=lambda x: x[1][4]))
# сортированный список по средней годовой прибыли
# print(sorted_companies)

avarage = all_av_margin / companies_number
print(f"Средняя прибыль компаний: {avarage:.2f}")
for name, margin in sorted_companies.items():
    if margin[-1] >= avarage:
        print(f'Средняя прибыль компании "{name}": {margin[4]} (выше среднего)')
    else:
        print(f'Средняя прибыль компании "{name}": {margin[4]} (ниже среднего')


print('#' * 30)
print(sys.version, sys.platform)
print('=' * 30)
show_memory(companies_number, companies, all_av_margin, sorted_companies, avarage, depth=3)

# ##############################
# Информация о системе: win32
# Информация об интерпритаторе Python: 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
# ==============================
#  'Значение '5', тип данных <class 'int'>, размер занимаемой памяти 28'
#  'Значение 'defaultdict(<class 'list'>, {'aaa': [12.0, 123.0, 124.0, 15.0, 68.5], 'bbb': [123.0, 1254.0, 15.0, 13.0, 351.25], 'ccc': [324.0, 25.0, 345.0, 1253.0, 486.75], 'ddd': [435.0, 56.0, 456.0, 34.0, 245.25], 'eee': [54.0, 65.0, 456.0, 456.0, 257.75]})', тип данных <class 'collections.defaultdict'>, размер занимаемой памяти 248'
# 		 'Значение '('aaa', [12.0, 123.0, 124.0, 15.0, 68.5])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('bbb', [123.0, 1254.0, 15.0, 13.0, 351.25])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('ccc', [324.0, 25.0, 345.0, 1253.0, 486.75])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('ddd', [435.0, 56.0, 456.0, 34.0, 245.25])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('eee', [54.0, 65.0, 456.0, 456.0, 257.75])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
#  'Значение '1409.5', тип данных <class 'float'>, размер занимаемой памяти 24'
#  'Значение 'OrderedDict([('aaa', [12.0, 123.0, 124.0, 15.0, 68.5]), ('ddd', [435.0, 56.0, 456.0, 34.0, 245.25]), ('eee', [54.0, 65.0, 456.0, 456.0, 257.75]), ('bbb', [123.0, 1254.0, 15.0, 13.0, 351.25]), ('ccc', [324.0, 25.0, 345.0, 1253.0, 486.75])])', тип данных <class 'collections.OrderedDict'>, размер занимаемой памяти 528'
# 		 'Значение '('aaa', [12.0, 123.0, 124.0, 15.0, 68.5])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('ddd', [435.0, 56.0, 456.0, 34.0, 245.25])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('eee', [54.0, 65.0, 456.0, 456.0, 257.75])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('bbb', [123.0, 1254.0, 15.0, 13.0, 351.25])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
# 		 'Значение '('ccc', [324.0, 25.0, 345.0, 1253.0, 486.75])', тип данных <class 'tuple'>, размер занимаемой памяти 64'
#  'Значение '281.9', тип данных <class 'float'>, размер занимаемой памяти 24'

# Вывод.
# При вводе данных о 5-ти предприятиях,  размер заполненного словаря defaultdict составляет 248 байт,
# размер OrderedDict - 528 байт