# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


max_sum = 0
number = ''
while True:
    N = input("Введите число: \n(Для завершения - нажмите 'Enter')\n")
    if N == '':
        break
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum > max_sum:
        max_sum = sum
        number = N
print(f"Число с наибольшей суммой цифр: {number}")
