from collections import namedtuple
from lesson_6.task_6_show_memory import show_memory

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f"Средняя прибыль = {average}")

print(f"Предприятия с прибылью выше среднего: ")
for comp in all_companies:
    if comp.profit > average:
        print(f"Компания {comp.name} заработала {comp.profit}")

print(f"Предприятия с прибылью нижу среднего: ")
for comp in all_companies:
    if comp.profit < average:
        print(f"Компания {comp.name} заработала {comp.profit}")


show_memory(QUARTERS, all_companies, total_profit, depth=3)

# # 'Значение '4', тип данных <class 'int'>, размер занимаемой памяти 28'
#  'Значение '{Company(name='d', quarters=(314, 436, 547, 234), profit=1531), Company(name='a', quarters=(1, 213, 45, 536), profit=795), Company(name='e', quarters=(234, 456, 2134, 654), profit=3478), Company(name='b', quarters=(123324, 23443, 65467, 5324), profit=217558), Company(name='c', quarters=(324, 346, 457, 568), profit=1695)}', тип данных <class 'set'>, размер занимаемой памяти 736'
#  'Значение '225057', тип данных <class 'int'>, размер занимаемой памяти 28'


 #
 # 'Значение '4', тип данных <class 'int'>, размер занимаемой памяти 28'
 # 'Значение '{Company(name='asd', quarters=(213, 234, 23, 4), profit=474), Company(name='ds', quarters=(42, 123, 243, 52642), profit=53050), Company(name='zcx', quarters=(312, 243, 543, 325), profit=1423), Company(name='zcc', quarters=(234, 214, 235324, 13524), profit=249296), Company(name='qwe', quarters=(132, 24, 243, 132), profit=531)}', тип данных <class 'set'>, размер занимаемой памяти 736'
	# 	 'Значение 'Company(name='asd', quarters=(213, 234, 23, 4), profit=474)', тип данных <class '__main__.Company'>, размер занимаемой памяти 72'
	# 			 'Значение 'asd', тип данных <class 'str'>, размер занимаемой памяти 52'
	# 			 'Значение '(213, 234, 23, 4)', тип данных <class 'tuple'>, размер занимаемой памяти 80'
	# 			 'Значение '474', тип данных <class 'int'>, размер занимаемой памяти 28'
	# 	 'Значение 'Company(name='ds', quarters=(42, 123, 243, 52642), profit=53050)', тип данных <class '__main__.Company'>, размер занимаемой памяти 72'
	# 			 'Значение 'ds', тип данных <class 'str'>, размер занимаемой памяти 51'
	# 			 'Значение '(42, 123, 243, 52642)', тип данных <class 'tuple'>, размер занимаемой памяти 80'
	# 			 'Значение '53050', тип данных <class 'int'>, размер занимаемой памяти 28'
	# 	 'Значение 'Company(name='zcx', quarters=(312, 243, 543, 325), profit=1423)', тип данных <class '__main__.Company'>, размер занимаемой памяти 72'
	# 			 'Значение 'zcx', тип данных <class 'str'>, размер занимаемой памяти 52'
	# 			 'Значение '(312, 243, 543, 325)', тип данных <class 'tuple'>, размер занимаемой памяти 80'
	# 			 'Значение '1423', тип данных <class 'int'>, размер занимаемой памяти 28'
	# 	 'Значение 'Company(name='zcc', quarters=(234, 214, 235324, 13524), profit=249296)', тип данных <class '__main__.Company'>, размер занимаемой памяти 72'
	# 			 'Значение 'zcc', тип данных <class 'str'>, размер занимаемой памяти 52'
	# 			 'Значение '(234, 214, 235324, 13524)', тип данных <class 'tuple'>, размер занимаемой памяти 80'
	# 			 'Значение '249296', тип данных <class 'int'>, размер занимаемой памяти 28'
	# 	 'Значение 'Company(name='qwe', quarters=(132, 24, 243, 132), profit=531)', тип данных <class '__main__.Company'>, размер занимаемой памяти 72'
	# 			 'Значение 'qwe', тип данных <class 'str'>, размер занимаемой памяти 52'
	# 			 'Значение '(132, 24, 243, 132)', тип данных <class 'tuple'>, размер занимаемой памяти 80'
	# 			 'Значение '531', тип данных <class 'int'>, размер занимаемой памяти 28'
 # 'Значение '304774', тип данных <class 'int'>, размер занимаемой памяти 28'