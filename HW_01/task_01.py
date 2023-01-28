# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input(('Введите трёхзначное число: ')))
if number<1000 and number>100 or number>-1000 and number<-100:
    num = abs(number)
    sum_of_three_digits = num % 10 + num//10%10 + num//100%10
    print("Сумма цифр числа {0} = {1}".format(number, sum_of_three_digits))
else:
    print('Число не является трёхзначным')