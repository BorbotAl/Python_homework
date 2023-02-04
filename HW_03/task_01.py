from random import randint as ri

list_length = int(input('Введите длину списка: '))
number_for_search = int(input('Введите искомое число: '))

user_list = []
count_of_eaquals = 0

for _ in range(list_length):
    new_int = ri(1, 100)
    user_list.append(new_int)
    if new_int == number_for_search:
        count_of_eaquals += 1
print (user_list)
if count_of_eaquals != 0:
    print (f'число {number_for_search} встречается в списке {count_of_eaquals} раз')
else:
    dif = 1
    flag = True
    while flag:
        for item in user_list:
            if number_for_search - item == dif or item - number_for_search == dif:
                print (f'Ближайшее к искомому числу {number_for_search} - число {item}')
                flag = False
                break
        dif += 1