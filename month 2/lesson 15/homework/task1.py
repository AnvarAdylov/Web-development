
def add(new_name, new_number, contacts_list):
    temp_dictionary = {'name': new_name, 'phone': new_number}
    contacts_list.append(temp_dictionary)


def commands(command):

    if command.lower() == 'add':
        print("Введите имя пользователя, которого вы хотите добавить:")
        new_user = input('> ')
        if duplicate_data(new_user, contacts):
            print("Этот контакт уже существует")
        else:
            print("Введите номер телефона контакта:")
            new_number = input('> ')
            add(new_user, new_number, contacts)
    elif command.lower() == 'list':
        list_all_contacts(contacts)
    elif command.lower() == 'edit':
        print("Введите имя пользователя, которого вы хотите изменить:")
        old_user = input('> ')
        if duplicate_data(old_user, contacts):
            print("Введите новое имя пользователя:")
            new_user = input('> ')
            if duplicate_data(new_user, contacts):
                print("Этот контакт уже существует")
            else:
                print("Введите новый номер телефона контакта:")
                new_number = input('> ')
                edit(old_user, new_user, new_number, contacts)
        else:
            print("Данного контакта нет в базе")
    elif command.lower() == 'delete':
        print("Введите имя пользователя, которого вы хотите удалить:")
        deleted_user = input('> ')

        if duplicate_data(deleted_user, contacts):
            print("Вы уверены, что хотите удалить контакт " + deleted_user)
            temp = input('> ')

            if (temp.lower() == 'yes' or
                    temp.lower() == 'ok' or temp.lower() == 'да'):
                delete(deleted_user, contacts)
                print("Контакт удален успешно")
        else:
            print("Данного контакта нет в базе")
    elif command.lower() == 'exit':
        exit()
    elif command.lower() == 'menu':
        programm_menu()
    elif command.lower() == 'find':
        print("Введите имя пользователя, которого вы хотите найти:")
        old_user = input('> ')
        temp = find(old_user, contacts)
        if temp is None:
            print("Не найден!")
        else:
            print("Name:          Phone:")
            print(contacts[temp]["name"].ljust(15) + contacts[temp]['phone'])
    elif command.lower() == 'sort':
        sort()
    else:
        print("Такой команды не существует.")


def delete(unwanted_name, contacts_list):
    contacts_list.pop(find(unwanted_name, contacts_list))


def duplicate_data(search_name, contacts_list):
    if find(search_name, contacts_list) is not None:
        return True
    else:
        return False


def edit(edit_name, new_name, new_number, contacts_list):
    temp = find(edit_name, contacts_list)
    contacts_list[temp]["name"] = new_name
    contacts_list[temp]["phone"] = new_number


def find(search_name, contacts_list):
    for i in range(len(contacts_list)):
        if contacts_list[i]['name'].lower() == search_name.lower():
            return i
    return None


def list_all_contacts(contacts_list):
    print("Name:          Phone:")
    for i in range(len(contacts_list)):
        print(contacts_list[i]["name"].ljust(15) + contacts_list[i]['phone'])


def main_programm():
    command = input('> ')
    commands(command)


def programm_menu():
    print("╔══════════════════════════════════════════╗")
    print("║        Добро пожаловать в программу      ║")
    print("║            Телефонная книга              ║")
    print("╠══════════════════════════════════════════╣")
    print("║ Список доступных комманд:                ║")
    print("║ list  - вывести контакты                 ║")
    print("║ menu - вывести меню снова                ║")
    print("║ find  - найти контакт                    ║")
    print("║ add   - добавить контакт                 ║")
    print("║ edit  - изменить контакт                 ║")
    print("║ delete - удалить контакт                 ║")
    print("║ exit   - выход                           ║")
    print("╚══════════════════════════════════════════╝")


def phone_book():
    programm_menu()
    while True:
        main_programm()


def sort():
    sorted_contacts = sorted(contacts, key=lambda x: x["name"])
    list_all_contacts(sorted_contacts)

contacts = [
    {
        "name": "John",
        "phone": "123456"
    },
    {
        "name": "Jane",
        "phone": "564321"
    },
    {
        "name": "Bob",
        "phone": "+1234"
    },
]

phone_book()
