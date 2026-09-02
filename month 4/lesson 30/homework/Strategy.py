from abc import ABC, abstractmethod


class PetStrategy():

    def feed(self, pet):
        if 0 <= pet.age < 6:
            YoungPet.decrease_hunger(self, pet)
            YoungPet.increase_health(self, pet)
            YoungPet.increase_mood(self, pet)
        elif 6 <= pet.age < 11:
            MidagePet.decrease_hunger(self, pet)
            MidagePet.increase_health(self, pet)
            MidagePet.increase_mood(self, pet)
        elif 11 <= pet.age:
            OldPet.decrease_hunger(self, pet)
            OldPet.increase_health(self, pet)
            OldPet.increase_mood(self, pet)

    def play(self, pet):
        if 0 <= pet.age < 6:
            YoungPet.increase_hunger(self, pet)
            YoungPet.increase_health(self, pet)
            YoungPet.increase_mood(self, pet)
        elif 6 <= pet.age < 11:
            MidagePet.increase_hunger(self, pet)
            MidagePet.increase_health(self, pet)
            MidagePet.increase_mood(self, pet)
        elif 11 <= pet.age:
            OldPet.increase_hunger(self, pet)
            OldPet.increase_health(self, pet)
            OldPet.increase_mood(self, pet)

    def heal(self, pet):
        if 0 <= pet.age < 6:
            YoungPet.increase_health(self, pet)
            YoungPet.increase_mood(self, pet)
        elif 6 <= pet.age < 11:
            MidagePet.increase_health(self, pet)
            MidagePet.increase_mood(self, pet)
        elif 11 <= pet.age:
            OldPet.increase_health(self, pet)
            OldPet.increase_mood(self, pet)


class HungerStrategy(ABC):
    @abstractmethod
    def increase_hunger(self, pet):
        pass

    @abstractmethod
    def decrease_hunger(self, pet):
        pass


class MoodStrategy(ABC):
    @abstractmethod
    def increase_mood(self, pet):
        pass

    @abstractmethod
    def decrease_mood(self, pet):
        pass


class HealthStrategy(ABC):
    @abstractmethod
    def increase_health(self, pet):
        pass

    @abstractmethod
    def decrease_health(self, pet):
        pass


class YoungPet(HungerStrategy, MoodStrategy, HealthStrategy):
    def increase_hunger(self, pet):
        pet.hunger_level -= 2

    def decrease_hunger(self, pet):
        pet.hunger_level += 10

    def increase_mood(self, pet):
        pet.mood_level += 10

    def decrease_mood(self, pet):
        pet.mood_level -= 2

    def increase_health(self, pet):
        pet.health_level += 10

    def decrease_health(self, pet):
        pet.health_level -= 2


class MidagePet(HungerStrategy, MoodStrategy, HealthStrategy):
    def increase_hunger(self, pet):
        pet.hunger_level -= 5

    def decrease_hunger(self, pet):
        pet.hunger_level += 5

    def increase_mood(self, pet):
        pet.mood_level += 5

    def decrease_mood(self, pet):
        pet.mood_level -= 5

    def increase_health(self, pet):
        pet.health_level += 5

    def decrease_health(self, pet):
        pet.health_level -= 5


class OldPet(HungerStrategy, MoodStrategy, HealthStrategy):
    def increase_hunger(self, pet):
        pet.hunger_level -= 10

    def decrease_hunger(self, pet):
        pet.hunger_level += 2

    def increase_mood(self, pet):
        pet.mood_level += 2

    def decrease_mood(self, pet):
        pet.mood_level -= 10

    def increase_health(self, pet):
        pet.health_level += 2

    def decrease_health(self, pet):
        pet.health_level -= 10
