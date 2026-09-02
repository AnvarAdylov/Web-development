from abc import ABC, abstractmethod


class AbsFigure(ABC):

    @abstractmethod
    def get_area(self):
        pass


class AbsSquare(ABC):

    @abstractmethod
    def get_side(self):
        pass


class AbsDoubleSquare(AbsFigure):

    @abstractmethod
    def build_double_square(self, square_1: AbsSquare, square_2: AbsSquare):
        pass


class AbstractDoubleSquare(AbsDoubleSquare):

    _area: float = 0

    @abstractmethod
    def build_double_square(self, square_1: AbsSquare, square_2: AbsSquare):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    def get_area(self):
        if self._area == 0:
            self._area = self.calculate_area()
        return self.calculate_area()


class Square(AbsSquare, AbsFigure):
    def __init__(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def get_area(self):
        return self.side**2


class DoubleSquare(AbstractDoubleSquare):
    def __init__(self, number=1):
        self.number = number

    def build_double_square(self, square_1: AbsSquare, square_2: AbsSquare):
        self.square1 = square_1
        self.square2 = square_2

    def get_area(self):
        return super().get_area()

    def calculate_area(self):
        return (self.square1.get_area() + self.square2.get_area())*self.number


square_1 = Square(10)

square_2 = Square(12)

double_square = DoubleSquare()

double_square.build_double_square(square_1, square_2)

print(f"Площадь double_square = {double_square.get_area()}")
