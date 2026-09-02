import Task1


class menu:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def do_it(self):
        print('perimeter: ' + self.rectangle.perimeter())
        print('area: ' + self.rectangle.area())
        self.rectangle.description()
