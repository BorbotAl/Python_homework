# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number = int(input('Введите номер своего билетика (шесть цифр): '))
if number > 99999 and number < 1000000:
    sum_of_first_three_digits = int(number//100000%10 + number//10000%10 + number//1000%10)
    sum_of_last_three_digits = int(number/100%10 + number//10%10 + number%10)
    print("Сумма первых трёх цифр: {0}".format(sum_of_first_three_digits))
    print("Сумма последних трёх цифр: {0}".format(sum_of_last_three_digits))
    if sum_of_last_three_digits == sum_of_first_three_digits:
        print('О, счастливчик!')
    else:
        print('Не повезло')
else:
    print('Не бывает билетиков с такими номерами')