# Вывести на экран 10 первых простых чисел используют функцию задания 1
# Подсказка:
# >>if is_prime(num):
#      print(num)


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def n_first_prime(n):
    found = 0
    num = 2
    while True:
        if is_prime(num):
            print(num)
            found += 1
        if found == n:
            break
        num += 1

n_first_prime(7)