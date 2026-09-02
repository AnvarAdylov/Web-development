import input_handler as ih
import product
import sys


class Wares():
    def __init__(self, file_name):
        self.input_file = file_name
        self.file_data = ih.Json_file_manager(file_name)
        self.wares = product.Product.convert(self.file_data.data)

    def get_goods(self):
        return self.wares

    def add_goods(self):
        the_id = input('введите уникальный идентификатор товара:\n> ')
        good_name = input('Напишите имя товара:\n> ')
        while True:
            starting_price = input('Напишите стартовую цену товара:\n> ')
            if ih.Validation.is_int(starting_price):
                starting_price = int(starting_price)
                break
        new_good = product.Product(the_id,
                                   good_name,
                                   starting_price,
                                   '', 'in_stock')
        self.wares.append(new_good)

    def display_wares(self):
        print(" № | id    | Товар          |Состояние | Цена       |код")
        for i in range(len(self.wares)):
            print(f' {i+1}' + ' | ' +
                  f'{self.wares[i].id:^5}' + ' | ' +
                  f'{self.wares[i].name:<14}' + ' | ' +
                  f'{self.wares[i].state.__str__()}' + ' | ' +
                  f'{self.wares[i].price:<10}' + ' | ' +
                  f'{self.wares[i].honorary_code:<30}')

    def display_ware(self, num):
        print(" id    | Товар          |Состояние | Цена       |код")
        print(f' {self.wares[num-1].id:^5}' + ' | ' +
              f'{self.wares[num-1].name:<14}' + ' | ' +
              f'{self.wares[num-1].state.__str__()}' + ' | ' +
              f'{self.wares[num-1].price:<10}' + ' | ' +
              f'{self.wares[num-1].honorary_code:<30}')


class Auction:
    def __init__(self):
        if ih.File_check.exist('products'):
            self.storage = Wares('products')
            self.storage.display_wares()
            self.add_prompt()
        else:
            print('Файл товаров отсутствует')
            self.storage = Wares('products')
            self.storage.display_wares()
            self.add_prompt()

        self.run()

    def run(self):
        self.storage.display_wares()
        while True:
            print('Введите номер интересуемого товара:')
            input_num = input('> ')
            cap = len(self.storage.wares)
            if ih.Validation.is_int(input_num):
                input_num = int(input_num)
                if input_num > cap or input_num < 0:
                    print("Неверный индекс! Введите другой")
                else:
                    break
        self.storage.display_ware(input_num)
        self.ware_sub_menu()
        self.sub_menu_handler(input_num)

    def ware_sub_menu(self):
        print('1. Выставить на аукцион ')
        print('2. Поднять цену. ')
        print('3. Выдать победителю ')
        print('4. Снять с торгов ')
        print('5. Отобразить информацию о товаре')
        print('6. Вернуться в меню товаров')
        print('7. Выйти')

    def sub_menu_handler(self, ware_num):
        product = self.storage.wares[ware_num-1]
        while True:
            while True:
                input_num = input('> ')
                if ih.Validation.is_int(input_num):
                    input_num = int(input_num)
                    if 0 > input_num > 7:
                        print("Неверный индекс!")
                    else:
                        break
            match input_num:
                case 1:
                    product.state.start_sale(self, product)
                    self.save_data()
                    self.storage.display_ware(ware_num)
                    self.ware_sub_menu()
                case 2:
                    product.state.raise_price(self, product)
                    self.save_data()
                    self.storage.display_ware(ware_num)
                    self.ware_sub_menu()
                case 3:
                    product.state.give_to_the_winner(self, product)
                    self.save_data()
                    self.storage.display_ware(ware_num)
                    self.ware_sub_menu()
                case 4:
                    product.state.withdraw(self, product)
                    self.save_data()
                    self.storage.display_ware(ware_num)
                    self.ware_sub_menu()
                case 5:
                    self.storage.display_ware(ware_num)
                    self.ware_sub_menu()
                case 6:
                    self.run()
                case 7:
                    self.save_data()
                    sys.exit()
                case _:
                    pass

    def add_prompt(self):
        print('Не хотите добавить новые товары вручную?')
        if input('>').lower() == 'yes':
            while True:
                self.storage.add_goods()
                self.save_data()
                print('Хотите добавить еще товар?')
                if input('>').lower() == 'no':
                    break
                self.storage.display_wares()

    def save_data(self):
        ih.Json_file_manager.rewrite_save(ih.Json_file_manager,
                                          'products', self.storage.wares)


Auction()
