
users_1 = [
    'elias@mail.ru',
    'kate@mil.com',
    'alex_1ro.ru',
    'sdgs@mail.com',
    'anton@mail.com',
    'kate19@23.com',
    'oleg13@mail.ua',
    'ole32g13ail.ua',
    'dsgsgsdg',
    '<a>agsdg</a>',
]
# Удалить из списка все не емейлы ("@")
a = list(users_1)

def check():
    value = users_1.pop()
    print(value)