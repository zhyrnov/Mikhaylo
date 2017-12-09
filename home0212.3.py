# Составить алгоритм увеличения всех трех, введённых с клавиатуры,переменных на 5,
# если среди них есть хотя бы две равные.
# В противном случае выдать ответ «равных нет».

while True:
    a = input('введите число 1= ')
    b = input('введите число 2= ')
    c = input('введите число 3= ')
    print('---' * 10)
    print('вы ввели 1=', a)
    print('вы ввели 2=', b)
    print('вы ввели 3=', c)
    print('---'*10)
    if a.isdigit() and b.isdigit() and c.isdigit():
        if a == b or b == c or a == c:
            a = int(a)
            b = int(b)
            c = int(c)
            print(a + 5, b + 5, c + 5)
            print('---' * 10)
        else:
            print('равных нет')
    else:
        print('''wrong entertry again''')
        print('---' * 10)










