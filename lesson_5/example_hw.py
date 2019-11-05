from collections import namedtuple

QUARTERS = 4
Company = namedtuple("Company", ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название {i}-й компании')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j+1}-й квартал')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

print()