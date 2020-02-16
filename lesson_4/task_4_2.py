# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
import cProfile

# Вариант 1 (перебор в цикле)
def loop(number):
    simple_list = []
    for i in range(2, number):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            simple_list.append(i)

    return simple_list


# Вариант 2 (Решето Эратосфена)

def eratosthen(number):
    sieve = [i for i in range(number)]
    sieve[1] = 0  # 1 не является простым

    for i in range(2, number):
        if sieve[i] != 0:
            j = i * 2
            while j < number:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]


# print(loop(200))
# print(eratosthen(200))

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.loop(102)"
# 1000 loops, best of 5: 365 usec per loop

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.eratosthen(102)"
# 1000 loops, best of 5: 31 usec per loop

#########################################################

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.loop(500)"
# 1000 loops, best of 5: 8.39 msec per loop

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.eratosthen(500)"
# 1000 loops, best of 5: 179 usec per loop

##########################################################

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.loop(1000)"
# 1000 loops, best of 5: 35.9 msec per loop

# python -m timeit -n 1000 -s "import task_4_2" "task_4_2.eratosthen(1000)"
# 1000 loops, best of 5: 383 usec per loop

# =============================================
# =============================================
# Разница по времени очевидна!


# cProfile.run('loop(1000)')

#         172 function calls in 0.042 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
#        1    0.042    0.042    0.042    0.042 task_4_2.py:6(loop)
#        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('eratosthen(1000)')

#         6 function calls in 0.001 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 task_4_2.py:21(eratosthen)
#        1    0.000    0.000    0.000    0.000 task_4_2.py:22(<listcomp>)
#        1    0.000    0.000    0.000    0.000 task_4_2.py:31(<listcomp>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
