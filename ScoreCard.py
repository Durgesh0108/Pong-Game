import datetime
import time
from email.policy import default
from turtle import Turtle, Screen

LEFT = "left"
RIGHT = "right"
CENTER = "center"
FONT = ["courier", 18, "bold"]
screen = Screen()


screen.tracer(0)
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.start_time = time.time()
        self.timer = 0
        self.player1 = screen.textinput(title="Player 1 Name", prompt="Enter Name of Player for Left Paddle: ")
        if (self.player1 == ""):
            self.player1 = "Player 1"
        self.player2 = screen.textinput(title="Player 2 Name", prompt="Enter Name of Player for Right Paddle: ")
        if (self.player2 == ""):
            self.player2 = "Player 2"
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.goto(-200, 270)
        self.write(f"{self.player1}: {self.l_score}", False, align="center", font=FONT)
        self.goto(200, 270)
        self.write(f"{self.player2}: {self.r_score}", False, align="center", font=FONT)
        # self.timer_function()
        self.hideturtle()

    def l_points(self):
        self.l_score += 1
        self.clear()
        self.update_Scoreboard()

    def r_points(self):
        self.r_score += 1
        self.clear()
        self.update_Scoreboard()

    # def timer_function(self):
    #     self.goto(0,270)
    #     self.timer = time.time() - self.start_time
    #     self.clear()
    #     self.write(f"Time: {int(self.timer)}", False, align="center", font=FONT)
        # self.clear()

    def game_over(self, player_name, player_score):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.hideturtle()
        self.clear()
        self.write(f"Game Over.",False, align=CENTER, font=FONT)
        self.goto(0, -30)
        self.write(f"{player_name} won the Game with {player_score} Points.",False, align=CENTER, font=FONT)
