# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint as RI

count_of_coins = int(input('Введите количество монет: '))

count_of_obverse = 0
count_of_reverse = 0
for _ in range (count_of_coins):
    coin = RI(0, 1)
    print(coin)
    if coin == 1:
        count_of_obverse += 1
    else:
        count_of_reverse += 1
if count_of_obverse == 0 or count_of_reverse == 0:
    print ('Все монеты лежат одинаково')
elif count_of_reverse <= count_of_obverse:
    print (f'Количество монет, которое надо перевернуть -> {count_of_reverse}')
else:
    print (f'Количество монет, которое надо перевернуть -> {count_of_obverse}')