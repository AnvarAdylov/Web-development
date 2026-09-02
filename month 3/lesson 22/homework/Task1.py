class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def description(self):
        print("Прямоугольник со сторонами %i и %i "
              % (self.length, self.width))
        print("Периметр прямоугольника: %i " % self.perimeter())
        print("Площадь прямоугольника: %i " % self.area())
