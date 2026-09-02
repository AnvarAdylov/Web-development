import random
import enum


class Cat:
    def __init__(self):
        self.satiety = random.randint(0, 100)
        self.max_satiety = random.randint(0, 100)

    def check(self):
        if self.satiety > self.max_satiety:
            print('Кот переел')
        elif self.satiety < self.max_satiety:
            print('Кот все еще голоден')
        elif self.satiety == self.max_satiety:
            print('Кот накормлен, поздравляем!')
        else:
            print('Кажись помер')

    def speak(self):
        print('Мяу')

    def status(self):
        print(f'Текущая сытость кота {self.satiety}/{self.max_satiety}')

    def feed(self, food):
        match food.lower():
            case Food.WISKAS.food_name:
                self.satiety = self.satiety + Food.WISKAS.satiety
            case  Food.SALMON.food_name:
                self.satiety = self.satiety + Food.SALMON.satiety
            case Food.ANCHOVY.food_name:
                self.satiety = self.satiety + Food.ANCHOVY.satiety
            case _:
                print('Такой еды у нас нет')


class Food(enum.Enum):
    WISKAS = (20, 'вискас')
    SALMON = (30, 'лосось')
    ANCHOVY = (10, 'анчоусы')

    def __init__(self, satiety, food_name):
        self.satiety = satiety
        self.food_name = food_name

    @staticmethod
    def random_food_item():
        constant_names = [
            attr for attr in dir(Food)
            if not callable(getattr(Food, attr))
            and not attr.startswith("__")
            ]
        pick = random.choice(constant_names)
        return getattr(Food[pick], 'food_name', None)


class programm():
    def __init__(self):
        kitty = Cat()
        kitty.status()
        if kitty.satiety > kitty.max_satiety:
            print('Коту нужна диета!')
        else:
            while True:
                kitty.speak()
                temp = Food.random_food_item()
                print("Робот кормит коту " + temp)
                kitty.feed(temp)
                kitty.check()
                kitty.status()
                if kitty.satiety >= kitty.max_satiety:
                    break


programm()
