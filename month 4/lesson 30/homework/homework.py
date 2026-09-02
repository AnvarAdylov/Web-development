from abc import ABC, abstractmethod
import Strategy
import random


class Pet(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger_level = 0
        self.mood_level = 0
        self.health_level = 0

    def feed(self, strategy):
        if random.randint(1, 6) == 6:
            print("Питомец отравился едой!")
            self.mood_level -= 10
            self.health_level -= 10
        else:
            strategy.feed(self)

    def play(self, strategy):
        strategy.play(self)

    def heal(self, strategy):
        strategy.heal(self)

    def is_dead(self):
        if (self.hunger_level < 0 or
           self.mood_level < 0 or
           self.health_level < 0):
            return True
        else:
            return False

    def __str__(self):
        return (
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Hunger Level: {self.hunger_level}, "
                f"Mood Level: {self.mood_level}, "
                f"Health Level: {self.health_level}"
                )


class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dinosaur(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)


class PetFactory:
    @staticmethod
    def create_pet(kind, name, age):
        if kind == "dog":
            return Dog(name, age)
        elif kind == "cat":
            return Cat(name, age)
        elif kind == "dinosaur":
            return Dinosaur(name, age)
        else:
            raise ValueError("Invalid pet kind")


def display(list_of_pets):
    for item in list_of_pets:
        print(item)


def check_pets(list_of_pets):
    for item in list_of_pets:
        if item.is_dead():
            print(f'Питомец {item.name} умер!')
            list_of_pets.remove(item)


class Tamagochi():
    def __init__(self):
        factory = PetFactory()
        strategy = Strategy.PetStrategy()
        pet_list = []
        dog = factory.create_pet("dog", "Goofy", 21)
        cat = factory.create_pet("cat", "Whiskers", 2)
        dino = factory.create_pet("dinosaur", "Nemo", 1)

        pet_list.append(dog)
        pet_list.append(cat)
        pet_list.append(dino)
        print()
        display(pet_list)
        while True:
            print("\nОпции:")
            print("1. Добавить нового питомца")
            print("2. Покормить питомца")
            print("3. Поиграть с питомцем")
            print("4. Вылечить питомца")
            print("5. Отобразить всех питомцев")
            print("6. Выход")

            choice = input("Введите ваш выбор: ")

            if choice == "1":
                while True:
                    print("Введите тип питомца (dog/cat/dinosaur): ")
                    pet_kind = input("> ").lower()
                    if pet_kind in ["dog", "cat", "dinosaur"]:
                        break
                    else:
                        print("Неверный тип питомца!")
                        print("Пожалуйста, введите dog/cat/dinosaur.")

                while True:
                    pet_name = input("Введите имя питомца: ")
                    if pet_name:
                        break
                    else:
                        print("Имя не может быть пустым!")

                while True:
                    pet_age = input("Введите возраст питомца: ")
                    if pet_age.isdigit():
                        pet_age = int(pet_age)
                        break
                    else:
                        print("Неверный возраст!")
                        print("Пожалуйста, введите корректный возраст.")

                new_pet = factory.create_pet(pet_kind, pet_name, pet_age)
                pet_list.append(new_pet)
                print("Новый питомец успешно добавлен!")

            elif choice == "2":
                print("Введите индекс питомца, которого вы хотите покормить: ")
                pet_index = int(input("> ")) - 1
                if 0 <= pet_index < len(pet_list):
                    pet_list[pet_index].feed(strategy)
                else:
                    print("Неверный индекс питомца!")
                    print("Пожалуйста, введите корректный индекс.")

            elif choice == "3":
                print("Введите индекс питомца, с которым вы хотите поиграть: ")
                pet_index = int(input("> ")) - 1
                if 0 <= pet_index < len(pet_list):
                    pet_list[pet_index].play(strategy)
                else:
                    print("Неверный индекс питомца!")
                    print("Пожалуйста, введите корректный индекс.")

            elif choice == "4":
                print("Введите индекс питомца, которого вы хотите вылечить: ")
                pet_index = int(input('> ')) - 1
                if 0 <= pet_index < len(pet_list):
                    pet_list[pet_index].heal(strategy)
                else:
                    print("Неверный индекс питомца!")
                    print("Пожалуйста, введите корректный индекс.")
            elif choice == "5":
                display(pet_list)
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор! Пожалуйста, введите число от 1 до 6.")
            check_pets(pet_list)
            display(pet_list)


Tamagochi()
