from turtle import Screen
from paddle import Paddle
from mid_line import Mid_line
from ScoreCard import Scoreboard
from Ball import Ball
from layout import Layout
import time
from music import Music

screen = Screen()
screen.bgcolor("red")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

layout = Layout()
mid_line = Mid_line()
l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
scoreboard = Scoreboard()
ball = Ball()
music = Music()

winning_score = screen.numinput(title="Winning Score", prompt="Set the Winning Score(Default: 5): ", default=5)

win_score = int(winning_score)

screen.listen()

# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_On = True

while game_is_On:
    time.sleep(0.06)
    screen.update()
    ball.move()
    

    if l_paddle.ycor() < ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
        l_paddle.go_up()
    elif l_paddle.ycor() > ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
        l_paddle.go_down()

    # if(l_paddle.ycor() >= -205 or l_paddle.ycor() <= 205):
    #     l_paddle.movement()

    # collision with upper and lower Wall
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.y_bounce()


    # # Collision of Paddle with Upper
    # if l_paddle.ycor() > 250 or r_paddle.ycor() > 250:
    #     l_paddle.stop_move()
    #     r_paddle.stop_move()


    # Collision with Paddle
    if ball.distance(l_paddle) < 50 or ball.xcor() < -350 or ball.distance(r_paddle) < 50 or ball.xcor() > 350:
        ball.increase_speed()
        ball.x_bounce()
        music.play_Paddle_Collision()

    # Increasing Score
    if ball.xcor() > 350:
        music.play_Wall_Collision()
        ball.reset_position()
        scoreboard.l_points()

    if ball.xcor() < -350:
        music.play_Wall_Collision()
        ball.reset_position()
        scoreboard.r_points()

    # Game Over and Final Result
    if scoreboard.l_score >= win_score:
        game_is_On = False
        music.play_Winning_Sound()
        Scoreboard.game_over(ball,scoreboard.player1, scoreboard.l_score)
    if scoreboard.r_score >= win_score:
        game_is_On = False
        music.play_Winning_Sound()
        Scoreboard.game_over(ball,scoreboard.player2, scoreboard.r_score)

screen.exitonclick()