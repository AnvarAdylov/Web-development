from abc import ABCMeta, abstractmethod
import code_generator as cg


class State(metaclass=ABCMeta):

    @abstractmethod
    def start_sale():
        pass

    @abstractmethod
    def raise_price():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def give_to_the_winner():
        pass


class Product:
    state: State

    def __init__(self, id, name, price, honorary_code, state):
        self.id = id
        self.name = name
        self.price = price
        self.original_price = price
        self.honorary_code = honorary_code
        self.state_from_string(state)

    def state_from_string(self, state):
        match state:
            case "in_stock":
                self.change_state(InStockState)
            case "for_sale":
                self.change_state(ForSaleState)
            case "sold":
                self.change_state(SoldState)
            case _:
                pass

    @staticmethod
    def convert(dict):
        list_of_products = []
        for item in dict:
            list_of_products.append(Product(item['id'],
                                            item['name'],
                                            item['price'],
                                            item['honorary_code'],
                                            item['state']))
        return list_of_products

    def change_state(self, state: State) -> None:
        self.state = state

    def __str__(self):
        str = f"№ | {self.id}\n"
        str = str + f"Товар | {self.name}\n"
        str = str + f"Цена| {self.price}\n"
        str = str + f"honorary_code | {self.honorary_code}\n"
        str = str + f"Состояние | {self.state.__str__()}"
        return str

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "honorary_code": self.honorary_code,
            "state": self.state.__str__()
        }


class InStockState(State):

    def raise_price(self, good: Product):
        print(f'Нельзя повысить цену у {good.name}')
        print('Товар еще не выставлен на продажу.')

    def start_sale(self, good: Product):
        good.change_state(ForSaleState)
        print(f'Товар {good.name} успешно выставлен на продажу.')

    def give_to_the_winner(self, good: Product):
        print('Нельзя отдать товар сразу со склада!')

    def withdraw(self, good: Product):
        print(f'нельзя снять с торгов товар {good.name}')
        print('Товар не участвует в аукционе.')

    def __str__():
        return 'in_stock'


class ForSaleState(State):

    def raise_price(self, good: Product, increment=500):
        good.price = good.price + increment
        print(f'Цена на товар {good.name} повышена на {increment}!')

    def start_sale(self, good: Product):
        print(f'Товар {good.name} уже участвует в торгах!')

    def give_to_the_winner(self, good: Product):
        if good.price == 0:
            print(f'Нельзя отдать товар {good.name} бесплатно!')
        else:
            good.change_state(SoldState)
            print(f'Товар {good.name} Продан за {good.price}')
            good.honorary_code = cg.CodeGenerator.generate(self, good)

    def withdraw(self, good: Product):
        if good.price == good.original_price:
            good.change_state(InStockState)
        else:
            print(f'Нельзя вернуть товар {good.name}!')
            print('Товар зарезервирован.')

    def __str__():
        return 'for_sale'


class SoldState(State):

    def raise_price(self, good: Product):
        print(f'Нельзя повысить цену у {good.name}')
        print('Товар уже был продан.')

    def start_sale(self, good: Product):
        print(f'Нельзя выставить на продажу {good.name}')
        print('Товар уже был продан.')

    def give_to_the_winner(self, good: Product):
        print('Товар уже был выдан победителю аукциона.')

    def withdraw(self, good: Product):
        print(f'Нельзя снять с торгов {good.name}')
        print('Товар уже был продан.')

    def __str__():
        return 'sold'
