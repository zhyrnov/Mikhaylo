# Решить рекурсивно задачу нахождения n-го числа фиббоначи (см. https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
n = int(input('fib(n), n = '))
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(n))