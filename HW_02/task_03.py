# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите число: '))
pow_of_2 = 1

while pow_of_2 <= number:
    print(pow_of_2)
    pow_of_2 *= 2