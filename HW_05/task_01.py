# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


def in_pow(num_1: int, num_2: int) -> int:
    if num_2 == 0:
        return 1
    if num_2 == 1:
        return num_1
    return num_1 * in_pow(num_1, num_2 - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень, в которую возведём число: '))

print(in_pow(a, b))