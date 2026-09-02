from abc import ABC, abstractmethod
import math


class AbsFigure(ABC):
    area: float = 0

    @abstractmethod
    def calculate_square(self):
        pass


class circle(AbsFigure):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def calculate_square(self):
        self.area = math.pi*(self.radius)**2


class triangle(AbsFigure):
    def __init__(self, name, base, height):
        self.name = name
        self.base = base
        self.height = height

    def calculate_square(self):
        self.area = self.base*self.height*(1/2)


class rectangle(AbsFigure):
    def __init__(self, name, length, width):
        self.name = name
        self.width = width
        self.length = length

    def calculate_square(self):
        self.area = self.width*self.length


def list_areas(figures):
    for i in range(len(figures)):
        figures[i].calculate_square()
    for i in range(len(figures)):
        print(f'{figures[i].name} area is {figures[i].area}')


listFigures = []
listFigures.append(circle('circle', 5))
listFigures.append(triangle('triangle', 2, 3))
listFigures.append(rectangle('rectangle', 5, 6))


list_areas(listFigures)
