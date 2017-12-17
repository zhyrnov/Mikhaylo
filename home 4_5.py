# Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран
# Пример:
# >> print_figure(‘треугольник’, 3)
# *
# **
# ***

x = int(input("""1. Квадрат
2. Треугольник
3. Ромб"""))
y = int(input('размер фигуры = '))


def print_figure():
    if x == 1:
        for i in range(y):
            print('*' * y, )
    if x == 2:
        for i in range(y):
            print('*' * (i+1))
    if x == 3:
        def zxc():
            print('*' * (y - i), end='')

        def cxz():
            print('*' * i, end='')

        for i in range(y):
            print(' ' * (y - i), end='')
            cxz()
            cxz()
            print(' ' * (y - i))
        for i in range(y):
            print(' ' * i, end='')
            zxc()
            zxc()
            print(' ' * i)


print_figure()