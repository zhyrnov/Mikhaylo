# Считать целое число с клавиатуры.
# Если число делится на 5 вывести на экран слово ‘fiz’,
# если число делится на 3 вывести ‘buz’,
# если число делится на 3 и 5 вывести ‘fizbuz’.

while True:

    a = int(input('a='))
    if a % 15 == 0:
        print('fizbuz')
    elif a % 5 == 0:
        print("fiz")
    elif a % 3 == 0:
        print('buz')
    else:
        print('try again')