import random


class Driver():
    NAMES = ['Jane', 'John', 'Gary', 'Eezekiel', 'Jeremy',
             'Charlie', 'Pim', 'Boss', 'Shlurpo', 'Glup']
    SURNAMES = ['Smith', 'King', 'Plutt', 'Shitto',
                'Marsh', 'Cartman', 'Crumb', 'Woombus']
    EXPERIENCE_CAP = 30
    AGE_CAP = 90

    def __init__(self, name, surname, experience, age):
        self.name = name
        self.surname = surname
        self.experience = experience
        self.age = age

    def __str__(self):
        str = f"Name: {self.name} {self.surname}\n"
        return str + f"Experience: {self.experience}\nAge: {self.age}"

    @staticmethod
    def random_driver():
        experience = random.randint(1, Driver.EXPERIENCE_CAP)
        return Driver(random.choice(Driver.NAMES),
                      random.choice(Driver.SURNAMES),
                      experience,
                      random.randint(experience + 15, Driver.AGE_CAP))
