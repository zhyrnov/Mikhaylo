# Написать программу реализующую хранилище информации о пользователях.
# Разбить логику по модулям: storage (функции get, add, get_storage), main (взаимодействие с пользователем)

#1.add
#2.get
#3.get_all
#>>1
#Email: Elias@mail.ru
#Login: eliasmir
#1.add
#2.get
#3.get_all
#>>2
#email: Elias@mail.ru

#Email: Elias@mail.ru
#Login: eliasmir

#1.add
#2.get
#3.get_all

login = None
mail = None
a = dict()
i = 0


def main():
    mail = input('mail= ')
    login = input('login= ')
    a['login', i] = login
    a['mail', i] = mail


def get(n):
    c = int(input('''
What you need?
1. Login
2. Mail
    you choice='''))
    print('*'*30)
    if c == 1:
        print('login =',a['login', n])
    if c == 2:
        print('mail =',a['mail',n])


def get_all():
    print('-'*30)
    for h in range(1, i+1):
        print('login', h, '=', a['login', h], 'mail', h, '=', a['mail', h])
        print('-'*30)


while True:
    try:
        l = int(input('''   ***Operation***
1. add mail and login
2. get mail or login
3. get all mail and login
    you choice ='''))
        print('*' * 30)
        if l == 1:
            i += 1
            main()
            print('*' * 30)
        if l == 2:
            print(i, 'people reg')
            print('*' * 30)
            n = int(input('what number need? ='))
            print('*' * 30)
            get(n)
            print('*' * 30)
        if l == 3:
            get_all()
    except ValueError:
        print('*'*30)
        print('wrong input')
        print('*'*30)
        continue
    if input('one more? (y/n)') == 'n':
        print('*' * 30)
        break
    else:
        print('*' * 30)