
def menu(self):
    print('''\nГлавное меню:
    1. Сохранить файл
    2. Показать контакты
    3. Создать контакт
    4. Изменить контакт
    5. Найти контакт
    6. Удалить контакт
    7. Выход''')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 8:
                return choice
            else:
                print('Введите число от 1 до 7')
        except:
            print('Вводи цифрами, а не буквами!')


def show_contacts(self, pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста!')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:20} {phone:<15} {comment:<20}')

def new_contact_input(self):
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_contact = {'name': name,
                   'phone': phone,
                   'comment': comment}
    return new_contact

def find_contact(self):
    find = input('Введите искомый элемент: ')
    return find

def input_id(self):
    ind = int(input('Введите индекс: '))
    return ind

