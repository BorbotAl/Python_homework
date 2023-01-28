# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input('Введите длину шоколадки: '))
width = int(input('Введите ширину шоколадки: '))
count = int(input('Сколько долек будем отламывать? : '))
if count/length >= 1 and count%length == 0 and count<length*width or count/width >= 1 and count%width == 0 and count<length*width:
    print('yes')
else:
    print('no')