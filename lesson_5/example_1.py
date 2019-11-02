# Задача: дан лог файл, нужно прочитать из N-последних строк, обработать, записать информацию в новый файл


from collections import deque, OrderedDict, defaultdict


N = 10  # Количество строк для чтения из файла
with open('file_1.txt', 'r', encoding='utf-8') as file:
    log = deque(file, N)

print(log)
counter = defaultdict(int)
output = OrderedDict()

for line in log:
    record = line[:-1]

    if not record.startswith('7'):
        counter[record] += 1
        output[record] = counter[record]  # сохраняет порядок записей

print(counter)
print(output)



