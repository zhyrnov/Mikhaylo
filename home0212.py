import math
while True:
    num1 = input('enter number 1=')
    num2 = input('enter number 2=')
    print('--------' * 10)
    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        print('num1=',num1,'num2=',num2)
        print('--------'*10)
        print ('''act Menu
        1. /
        2. * 
        3. - 
        4. +
        5. **
        6. con(num1+num2)
        7. sin(num1+num2)
        ''')
        print('--------' * 10)
        choice = float(input('your choice:'))
        print('--------'*10)
        if choice == 1:
            print(num1,'/',num2,'=')
            print (round((num1 / num2),3))
            print('--------' * 10)
        elif choice == 2:
            print(num1, '*', num2, '=')
            print(round((num1 * num2),3))
            print('--------' * 10)

        elif choice == 3:
            print(num1, '-', num2, '=')
            print(round((num1 - num2), 3))
            print('--------' * 10)

        elif choice == 4:
            print(num1, '+', num2, '=')
            print(round((num1 + num2), 3))
            print('--------' * 10)

        elif choice == 5:
            print(num1, '**', num2, '=')
            print(round((num1 ** num2), 3))
            print('--------' * 10)

        elif choice == 6:
            print('cos','(',num1,'+', num2,')', '=')
            y = math.cos(num1 + num2)
            print(round(y, 3))
            print('--------' * 10)
        elif choice == 7:
            print('sin','(',num1,'+', num2,')', '=')
            x = math.sin(num1 + num2)
            print(round(x,3))
            print('--------' * 10)
        else:
            print('''invalid choice....
                  try again....'
                  choice main menu!''')
    else:
        print("It's not number! Try again!")
        print('--------' * 10)