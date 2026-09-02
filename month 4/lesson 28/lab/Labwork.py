import datetime
import random
import math


class Store:
    def __init__(self):
        self.products = Product_generator(20).products

    def do_inspection(self):
        print()
        print()
        print(f'{'Inspection result:':^60}')
        print()
        print()
        print(f' {'Product':^9}|{'Delivered at':^17}|'
              f'{'Stored at':^12}|{'Shelf life days':^17}|{' Fresh'}')
        print("----------+-----------------+------------+-----------------"
              "+-------")
        for i in range(len(self.products)):
            print(f' {self.products[i].name:^8} | '
                  f'{self.products[i].delivery_timestamp.strftime("%b %d, %Y"):^15} | '
                  f'{self.products[i].storage_place:^10} | '
                  f'{self.products[i].storage_life_days:>15} | '
                  f'{str(self.products[i].is_fresh()):<7}')
        print("----------+-----------------+------------+-----------------"
              "+-------")
        return None

    @staticmethod
    def get_random_delivery_time():
        random_number = random.randint(0, 200)
        delivery_timestamp = (datetime.datetime.now() -
                              datetime.timedelta(days=random_number))
        return delivery_timestamp

    @staticmethod
    def get_random_storage_place():
        Storage = ["Icebox", "Showcase"]
        return random.choice(Storage)


class Product:
    PRODUCTS = ['Milk', 'Salt', 'Fish', 'Corn', 'Stew']

    def __init__(self,
                 delivery_timestamp,
                 storage_place,
                 storage_life_days,
                 name):
        self.delivery_timestamp = delivery_timestamp
        self.storage_place = storage_place
        self.storage_life_days = storage_life_days
        self.name = name

    def is_fresh(self):
        current_time = datetime.datetime.now()
        delta = current_time - self.delivery_timestamp
        return bool(delta.days <= self.storage_life_days)

    @staticmethod
    def random():
        random_product = random.choice(Product.PRODUCTS)
        if random_product == 'Milk':
            product = Milk()
        elif random_product == 'Salt':
            product = Salt()
        elif random_product == 'Fish':
            product = Fish()
        elif random_product == 'Corn':
            product = Corn()
        elif random_product == 'Stew':
            product = Stew()
        return product


class Milk(Product):
    def __init__(self):
        timestamp = Store.get_random_delivery_time()
        storage = Store.get_random_storage_place()
        if storage == 'Icebox':
            shelf_life = 60
        elif storage == 'Showcase':
            shelf_life = 30
        super().__init__(timestamp, storage, shelf_life, 'Milk')


class Salt(Product):
    def __init__(self):
        timestamp = Store.get_random_delivery_time()
        storage = Store.get_random_storage_place()
        if storage == 'Icebox':
            shelf_life = math.inf
        elif storage == 'Showcase':
            shelf_life = math.inf
        super().__init__(timestamp, storage, shelf_life, 'Salt')


class Fish(Product):
    def __init__(self):
        timestamp = Store.get_random_delivery_time()
        storage = Store.get_random_storage_place()
        if storage == 'Icebox':
            shelf_life = 20
        elif storage == 'Showcase':
            shelf_life = int(20/6)
        super().__init__(timestamp, storage, shelf_life, 'Fish')


class Corn(Product):
    def __init__(self):
        timestamp = Store.get_random_delivery_time()
        storage = Store.get_random_storage_place()
        if storage == 'Icebox':
            shelf_life = 150
        elif storage == 'Showcase':
            shelf_life = 150
        super().__init__(timestamp, storage, shelf_life, 'Corn')


class Stew(Product):
    def __init__(self):
        timestamp = Store.get_random_delivery_time()
        storage = Store.get_random_storage_place()
        if storage == 'Icebox':
            shelf_life = 180
        elif storage == 'Showcase':
            shelf_life = 180
        super().__init__(timestamp, storage, shelf_life, 'Stew')


class Product_generator:
    def __init__(self, amount):
        self.products = []
        for i in range(amount):
            self.products.append(Product.random())


store = Store()
store.do_inspection()
