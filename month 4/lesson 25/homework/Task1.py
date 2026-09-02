import turtle
from shapes import shape


class Shape_drawing():
    def __init__(self):
        self.triangle('#800080', '#00FF00', [0, 0], 90, 50)
        self.square('#800080', '#FFFF00', [60, 0], 90, 50)
        self.pentagon('#800080', '#FF0000', [120, 0], 90, 50)

    def triangle(self, border, fill, coordinates, heading, side):
        turtle.penup()
        triangle = shape.Shape(border, fill, coordinates, heading)
        triangle.draw()
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(60)
        turtle.forward(side)
        turtle.setheading(300)
        turtle.forward(side)
        turtle.setheading(180)
        turtle.forward(side)
        turtle.end_fill()
        turtle.penup()

    def square(self, border, fill, coordinates, heading, side):
        turtle.penup()
        square = shape.Shape(border, fill, coordinates, heading)
        square.draw()
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(side)
        turtle.setheading(0)
        turtle.forward(side)
        turtle.setheading(270)
        turtle.forward(side)
        turtle.setheading(180)
        turtle.forward(side)
        turtle.end_fill()
        turtle.penup()

    def pentagon(self, border, fill, coordinates, heading, side):
        turtle.penup()
        pentagon = shape.Shape(border, fill, coordinates, heading)
        pentagon.draw()
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(side)
            turtle.right(72)
        turtle.end_fill()
        turtle.penup()
        turtle.penup()


Shape_drawing()
