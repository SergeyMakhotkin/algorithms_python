# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict, OrderedDict

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
