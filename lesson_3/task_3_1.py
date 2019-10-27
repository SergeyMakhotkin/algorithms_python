# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

count_dict = {key: 0 for key in range(2,10)}  # словарь со счетчиками
for number in range(2,100):
    for i in range(2,10):
        if not number % i:
            count_dict[i] += 1
for key, value in count_dict.items():
    print(f'{value} чисел кратно {key}')


