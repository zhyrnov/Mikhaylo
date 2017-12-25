# 2.
users_1 = [
    'elias@mail.ru',
    'kate@mil.com',
    'alex_1@ro.ru',
    'sdgs@mail.com',
    'anton@mail.com',
    'kate19@23.com',
    'oleg13@mail.ua',
]
users_2 = [
    'diana123@ro.ru',
    'anton@mail.com',
    'elias@mail.ru',
    'kate156@mil.com',
    'oleg13@mail.ua',
    'sdgs@mail.com',
    'kate19@23.com',
]
# вывести меилы которые есть в двух списках

a ={*users_1}
b ={*users_2}
result = a & b

print(*result, sep=' | ')