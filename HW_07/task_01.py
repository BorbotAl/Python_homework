# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

poem = input('Напишите кричалку: ')
poem_list = poem.split()

def syllable (str_elem: str) -> int:
    vowels = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
    count_of_syllables = 0
    for liter in str_elem:
        if liter in vowels:
            count_of_syllables += 1
    return count_of_syllables

list_syllable = list(map(syllable, poem_list))

if len(set(list_syllable)) == 1:
    print('Парам пам-пам')
else:
   print('Пам парам')