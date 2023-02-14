# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as RI

count = int(input('Введите длину списка: '))
min_number = int(input('Введите минимальное значение диапазона: '))
max_number = int(input('Введите максимальное значение диапазона: '))

if min_number < max_number:
    user_list = list()
    list_of_index_in_range = list()
    for i in range(count):
        temp = RI(0, 10)
        user_list.append(temp)
        if temp in range(min_number, max_number+1):
            list_of_index_in_range.append(i)
    print(f'Исходный список: {user_list}')
    print(f'Список индексов элементов, которые лежат в диапазоне от {min_number} до {max_number} : {list_of_index_in_range}')
else:
    print('Диапазон является пустым множеством')
