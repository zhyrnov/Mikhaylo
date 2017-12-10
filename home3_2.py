# Вывести на экран фигуры со звездочек
# (Ромб, Елочка, Треугольник, Квадрат, ступеньки)
a = int(input('longest = '))


def jcb():
    for i in range(a):
        print('*' * a, )


def qwe():
    for i in range(a):
        print('*' * i)


def asd():
    for i in range(a):
        print('*' * (a - i))


# квадрат
jcb()
print('kvadrat')
# треугольник
qwe()
print('treugolnik 1')
asd()
print('treugolnik 2')


# Ромб
def zxc():
    print('*' * (a - i), end='')


def cxz():
    print('*' * i, end='')


for i in range(a):
    print(' ' * (a-i), end='')
    cxz()
    cxz()
    print(' ' * (a-i))
for i in range(a):
    print(' ' * i, end='')
    zxc()
    zxc()
    print(' ' * i)
print('romb')


# ступеньки
def q():
    print('*',end='')


def w():
    print('-',end='')


def e():
    print('')


def ww():
    w()
    w()


def qq():
    q()
    q()
    q()


def www():
    ww()
    ww()


def zzz():
    qq()
    www()
    e()
    ww()
    q()
    www()
    e()
    ww()
    qq()
    ww()
    e()
    www()
    qq()
    e()


zzz()
print('end')