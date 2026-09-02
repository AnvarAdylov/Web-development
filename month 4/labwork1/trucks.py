from abc import ABCMeta, abstractmethod
import random
import driver


class State(metaclass=ABCMeta):

    @abstractmethod
    def change_driver():
        pass

    @abstractmethod
    def start_run():
        pass

    @abstractmethod
    def start_repair():
        pass


class Truck():
    state: State
    STATES = ["base", "run", "repair"]

    def __init__(self, id, name, driver, state):
        self.id = id
        self.name = name
        self.driver = driver
        self.state_from_string(state)

    @staticmethod
    def convert(dict):
        list_of_trucks = []
        for item in dict:
            list_of_trucks.append(Truck(item['id'],
                                  item['name'],
                                  item['driver'],
                                  item['state_name']))
        return list_of_trucks

    def change_state(self, state: State) -> None:
        self.state = state

    def state_from_string(self, state):
        match state:
            case "run":
                self.change_state(InRunState)
            case "base":
                self.change_state(InBaseState)
            case "repair":
                self.change_state(InRepairState)
            case _:
                pass

    def change_driver(self):
        self.new_driver = driver.Driver.random_driver()
        self.driver = self.new_driver.name

    def __str__(self):
        str = f"№ | {self.id}\n"
        str = str + f"Марка| {self.name}\n"
        str = str + f"Водитель| {self.driver}\n"
        str = str + f"Состояние| {self.state.__rus_str__()}"
        return str

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "driver": self.driver,
            "state_name": self.state.__str__()
        }


class InBaseState(State):
    def change_driver(self, truck: Truck):
        truck.change_driver()
        print('водитель поменян успешно!')

    def start_run(self, truck: Truck):
        truck.change_state(InRunState)
        print(f'Грузовик “{truck.name}” - На маршруте')

    def start_repair(self, truck: Truck):
        truck.change_state(InRepairState)
        print(f'Грузовик “{truck.name}” - В ремонте')

    def __str__():
        return 'base'

    def __rus_str__():
        return 'на базе'


class InRunState(State):
    def change_driver(self, truck: Truck):
        print('ошибкa, так как водителя нельзя менять в пути')

    def start_run(self, truck: Truck):
        print('Oшибкa - грузовик и так в пути')

    def start_repair(self, truck: Truck):
        truck.change_state(InRepairState)
        print(f'Грузовик “{truck.name}” - В ремонте')

    def __str__():
        return 'run'

    def __rus_str__():
        return 'в дороге'


class InRepairState(State):
    def change_driver(self, truck: Truck):
        truck.change_driver()
        print('водитель поменян успешно!')

    def start_run(self, truck: Truck):
        truck.change_state(random.choice([InRunState, InBaseState]))
        print(f'Грузовик “{truck.name}” - На маршруте')

    def start_repair(self, truck: Truck):
        print('Oшибкa - уже в ремонте!')

    def __str__():
        return 'repair'

    def __rus_str__():
        return 'в ремонте'
