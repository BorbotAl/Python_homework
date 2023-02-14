# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_list (first_num: int, count: int, dif: int) -> list:
    arithm_prog = [first_num]
    for i in range(count-1):
        arithm_prog.append(arithm_prog[i]+dif)
    return arithm_prog

num = int(input('Введите первый элемент арифметической прогрессии: '))
differ = int(input('Введите разность между элементами арифметической прогрессии: '))
count_nums = int(input('Введите количество элементов арифметической прогрессии: '))

print(fill_list(num, count_nums, differ))