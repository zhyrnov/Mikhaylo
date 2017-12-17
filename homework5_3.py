# Написать функцию, которая выводит двухмерный список в виде таблицы
# Пример
# >>print_list([[222, 113], [456, 500]])
# —————
# | 222 | 113 |
# —————
# | 456 | 500 |
# —————
import math
import random
n = int(input('n='))


def gen_list(n):
    a = []
    b = []
    c = []
    for _ in range(n):
        a.append(random.randint(100,999))
        b.append(random.randint(100, 999))
        c.append(random.randint(100,999))
    print([a, b, c])
    return [a, b, c]


table = gen_list(n)
print(max(table, key=sum))
print('----')


def print_list(table):
    print('-'*(len(table)*3 +(len(table)-1)*3 + 4))
    for line in table:
        print('| ', end='')
        for number in line:
            print(number, '| ',end='')
        print()
        print('-' * (len(table) * 3 +(len(table) - 1) * 3 + 4))

print_list(table)
