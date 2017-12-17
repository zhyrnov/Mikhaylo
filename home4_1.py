# Написать функцию is_prime(a), Которая принимает число и
# возвращает True или False в зависимости от того,
# простое это число или нет (см. https://ru.wikipedia.org/wiki/Простое_число)
# Пример:
# >>is_prime(3)
# >>True
# >>is_prime(4)
# >>False

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


print(7, (is_prime(7)))
print(13, (is_prime(13)))

