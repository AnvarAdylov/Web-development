import input_handler
import trucks
import sys


class Autobase():
    def __init__(self):
        while True:
            file_input = input('Write the name of the input file \n> ')
            if input_handler.File_check.exist(file_input):
                break
            else:
                print('Такого файла нет!')
        while True:
            file_output = input('Write the name of the output file \n> ')
            if input_handler.File_check.exist(file_output):
                break
            else:
                print('Такого файла нет!')
        self.file_input = file_input
        self.file_output = file_output
        self.file_data = input_handler.Json_file_manager(file_input)
        self.trucks = trucks.Truck.convert(self.file_data.data)

        while True:
            self.menu()
            command = input('> ')
            self.menu_choice(command)

    def menu_choice(self, choice):
        if choice == '1':
            self.display_trucks()
        elif choice == '2':
            while True:
                truck_id = input('Введите сериальный номер грузовика:\n> ')
                if input_handler.Validation.is_int(truck_id):
                    break
            print(self.truck_by_id(int(truck_id)))
        elif choice == '3':
            print('Укажите номер грузовика и состояние через пробел:')
            user_input = input('> ')
            print('Обновление состояния грузовика')
            inputs = user_input.split()
            if len(inputs) != 2:
                print("Неверный формат ввода")
                print("Пожалуйста, введите число, а затем командное слово.")
            else:
                try:
                    number = int(inputs[0])
                    state = inputs[1].lower()
                    truck = self.trucks[number-1]
                    if state not in trucks.Truck.STATES:
                        print("Недопустимое командное слово.")
                        print("Пожалуйста, введите разрешенную команду:")
                        print(trucks.Truck.STATES)
                    else:
                        self.alter_state(truck, state)
                except ValueError:
                    print("Неверное число.")
                    print("Пожалуйста, введите допустимое целое число.")
            self.save_truck_data()
        elif choice == '4':
            while True:
                print("Введите id грузовика если хотите сменить водителя:")
                id_for_swap = input("> ")
                if input_handler.Validation.is_int(id_for_swap):
                    id_for_swap = int(id_for_swap)
                    break
            for item in self.trucks:
                if item.id == id_for_swap:
                    item.state.change_driver(self, item)
            self.save_truck_data()
        elif choice == '5':
            self.save_truck_data()
            sys.exit()
        else:
            return Exception

    def menu(self):
        print('Меню:')
        print("    1.Отобразить текущее состояние грузовиков")
        print("    2.Показать данные грузовика по id")
        print("    3.Обновить состояние грузовика")
        print("    4.Поменять водителя грузовика")
        print("    5.Завершить программу и выгрузить все данные")

    def display_trucks(self):
        print(" №  | Грузовик        | Водитель   | Состояние ")
        for i in range(len(self.trucks)):
            print(f'{self.trucks[i].id:^3}' + ' | ' +
                  f'{self.trucks[i].name:<15}' + ' | ' +
                  f'{self.trucks[i].driver:<10}' + ' | ' +
                  f'{self.trucks[i].state.__rus_str__()}')

    def truck_by_id(self, id):
        for item in self.trucks:
            if item.id == id:
                return item
        return "Грузовик не найден"

    def alter_state(self, truck: trucks.Truck, state):
        if truck.state is None:
            truck.state_from_string(truck.state)
        match state:
            case "run":
                truck.state.start_run(self, truck)
            case "base":
                truck.change_state(trucks.InBaseState)
            case "repair":
                truck.state.start_repair(self, truck)
            case _:
                pass

    def save_truck_data(self):
        input_handler.Json_file_manager.rewrite_save(self.file_data,
                                                     self.file_output,
                                                     self.trucks)


Autobase()
