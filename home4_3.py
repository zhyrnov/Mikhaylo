# Написать функцию, которая выводит на экран n первых четных чисел.
# >>func(3):
# >>2, 4, 6


def func(n):

    for i in range(1, 2 * n, 2):
        print(i+1)

print(func(3))
