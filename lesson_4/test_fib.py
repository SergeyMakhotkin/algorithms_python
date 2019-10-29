def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        try:
            assert item == func(i)
            print(f"Тест {i} ok")
        except AssertionError:
            print(f"Ошибка при значении {i}!!!")


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


test_fib(fib)