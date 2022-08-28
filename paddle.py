from time import sleep
from turtle import Turtle, ycor

PADDLE_Movement = 30


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.y_move = 30

    def go_up(self):
        new_y = self.ycor() + PADDLE_Movement
        if (self.ycor() <= 205):
            self.goto(self.xcor(), new_y)
        # if (self.ycor() <= 205):
        #     self.sety(self.pos()[1] + 20)

    def go_down(self):
        new_y = self.ycor() - PADDLE_Movement
        if (self.ycor() >= -205):
            self.goto(self.xcor(), new_y)
        # if (self.ycor() >= -205):
        #     self.sety(self.pos()[1] - 20)

    def movement(self):
        self.y_move *= -1


    def move(self):
        self.goto(self.xcor(),self.ycor() + PADDLE_Movement)
        # self.computer_move()

    def stop_move(self):
        self.goto(self.xcor(), self.ycor())
