# Написать функцию is_prime(a), Которая принимает число и
# возвращает True или False в зависимости от того,
    # простое это число или нет (см. https://ru.wikipedia.org/wiki/Простое_число)
# Пример:
# >>is_prime(3)
# >>True
# >>is_prime(4)
# >>False

while True:
    a = int(input('number = '))
    def is_prime(a):
        if a / 2 or a / 3:
            return False
        elif a / 1 and a / a:
            return True
    print(is_prime(a))


#
#while True:
#    x = int(input('x='))
#    def isprime(x):
#        if x > 3 and x % 2 == 0 or x <= 1:
#            return False
#        for i in range(3, int(x ** 0.5) + 1, 2):
#            if x % i == 0:
#                return False
#        return True
#
#    print(isprime(x))
