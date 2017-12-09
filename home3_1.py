#3. Вывести таблицу умножения на экран.

a = 1
b =1

while True:
    for a in range(1,10):
        print(a, '*', b, '=', a * b)
    if a == 9:
        b += 1
    if b == 10:
            break

#