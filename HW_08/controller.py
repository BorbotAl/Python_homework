from db_manager import PhoneBook
import view

phones = PhoneBook('new_phones.txt')


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                phones.save()
                print('\nИзменения сохранены!')
            case 2:
               pb = phones.get()
               view.show_contacts(pb)
            case 3:
               new = view.new_contact_input()
               phones.add(new)
            case 4:
                pb = phones.get()
                view.show_contacts(pb)
                ind = view.input_id()
                contact = view.new_contact_input()
                phones.change_contact(ind, contact)

            case 5:
                find = view.find_contact()
                result = phones.find(find)
                view.show_contacts(result)
            case 6:
                pb = phones.get()
                view.show_contacts(pb)
                ind = view.input_id()
                phones.delete_contact(ind)
            case 7:
                print('До свидания!')
                break

