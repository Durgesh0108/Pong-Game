from email.policy import default
from turtle import Turtle, Screen

LEFT = "left"
RIGHT = "right"
CENTER = "center"
FONT = ["courier", 18, "bold"]
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
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
        self.hideturtle()

    def l_points(self):
        self.l_score += 1
        self.clear()
        self.update_Scoreboard()

    def r_points(self):
        self.r_score += 1
        self.clear()
        self.update_Scoreboard()

    def game_over(self, player_name, player_score):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.hideturtle()
        self.clear()
        self.write(f"Game Over. {player_name} won the Game with {player_score} Points.", False, align=CENTER, font=FONT)
