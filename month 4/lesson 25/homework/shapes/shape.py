import turtle


class Shape():
    def __init__(self, border, fill, coordinates, heading):
        self.border = border
        self.fill = fill
        self.coordinates = coordinates
        self.heading = heading

    def draw(self):
        turtle.goto(self.coordinates[0], self.coordinates[1])
        turtle.setheading(self.heading)
        turtle.pencolor(self.border)
        turtle.fillcolor(self.fill)

    def __str__(self):
        return (f"A figure set at coordinates:{self.coordinates}" +
                f"\n {self.fill} colored with {self.border} borders" +
                f"\n Facing angle of {self.heading} degrees")
