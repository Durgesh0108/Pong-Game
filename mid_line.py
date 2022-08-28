from turtle import Turtle


class Mid_line(Turtle):
    def __init__(self):
        super(Mid_line, self).__init__()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for x in range(15):
            self.pendown()
            self.forward(21)
            self.penup()
            self.forward(20)
        self.hideturtle()


