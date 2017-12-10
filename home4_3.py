# Написать функцию, которая выводит на экран n первых четных чисел.
# >>func(3):
# >>2, 4, 6

x = int(input())


def func():
    for i in range(2,x,2):
       print(i)
func()
print('end')