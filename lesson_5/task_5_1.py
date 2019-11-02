# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, defaultdict

# Companies = namedtuple('Companies', 'name, margin', defaults=['unknown_name', 0])

number = int(input("Введите количество предприятий: \n"))
companies = defaultdict(list)

for i in range(number):
    name = input(f"Введите название {i+1}-компании: \n")
    margin = float(input(f"Введите прибыль компании '{name}': \n"))
    # companies[name] = margin
    companies[name].append(margin)
print(companies)

