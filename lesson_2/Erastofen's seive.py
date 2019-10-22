print("Решето Эрастофена\n", '#' * 15, '\n')
n = int(input('Введите число, до которого нужно найти простые числа: \n'))
sieve = [i for i in range(n)]
sieve[1] = 0
for i in range(n):
    if sieve[i] != 0:
        j = i * 2
        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]
print(result)