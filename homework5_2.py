# Написать функцию, которая генерирует список списков (двух мерный массив)
# размерности NxN заполненный случайными числами от 100 до 999
# (использовать функцию random.randint(100, 999))
# пример
# >>gen_list(2)
# [[222, 113], [456, 500]]

import random


def gen_list(n):
    a = []
    b = []
    for _ in range(n):
        a.append(random.randint(100,999))
    for _ in range(n):
        b.append(random.randint(100, 999))

    print([a,b])

gen_list()