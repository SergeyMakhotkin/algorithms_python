# 4. Определить, какое число в массиве встречается чаще всего.

import random

n = int(input("Введите количество элементов в массиве: \n"))
arr = [random.randint(0, 10) for _ in range(n)]
item_dict = {}
max_count = 0
max_count_key = ''
for i in range(n):
    item_count = 0
    for item in arr:
        if item == arr[i]:
            item_count += 1
            item_dict[item] = item_count
print(item_dict)
for key, value in item_dict.items():
    if value > max_count:
        max_count = value
        max_count_key = key
print(f'Число {max_count_key} встретилось {item_dict[max_count_key]} раз')


