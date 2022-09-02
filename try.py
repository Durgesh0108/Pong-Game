import time
import turtle
from turtle import Screen

from Ball import Ball
from ScoreCard import Scoreboard
from layout import Layout
from mid_line import Mid_line
from music import Music
from paddle import Paddle

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

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_On = True

# time_limit = 0

is_paused = False

# Final = turtle.Turtle()
# timer = turtle.Turtle()
#
# start_time = time.time()
# final_time = 0
# elapsed_time = int(time.time() - start_time)


def pause():
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True


screen.onkey(pause, "space")

while game_is_On:
    # if timer is on:
    # elapsed_time = int(time.time() - start_time)
    # timer.penup()
    # timer.color("White")
    # timer.goto(0, 270)
    # timer.clear()
    # timer.write(f"Time: {elapsed_time}", False, align="center", font=("courier", 18, "bold"))
    # timer.hideturtle()
    # print(elapsed_time)
    if not is_paused:
        time.sleep(0.06)
        screen.update()
        ball.move()

        # elapsed_time = int(time.time() - start_time)
        # timer.penup()
        # timer.color("White")
        # timer.goto(0, 270)
        # timer.clear()
        # timer.write(f"Time: {elapsed_time}", False, align="center", font=("courier", 18, "bold"))
        # timer.hideturtle()

        # print(elapsed_time)

        # collision with upper and lower Wall
        if ball.ycor() > 250 or ball.ycor() < -250:
            ball.y_bounce()

        # Collision with Paddle
        if ball.distance(l_paddle) < 50 or ball.xcor() < -350 or ball.distance(r_paddle) < 50 or ball.xcor() > 350:
            ball.increase_speed()
            ball.x_bounce()
            music.play_Paddle_Collision()

        # if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50):
        #     ball.increase_speed()
        #     ball.x_bounce()
        #     music.play_Paddle_Collision()
        #
        # if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50):
        #     ball.increase_speed()
        #     ball.x_bounce()
        #     music.play_Paddle_Collision()

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
            # game_is_On = False
            is_paused = False
            music.play_Winning_Sound()
            Scoreboard.game_over(ball, scoreboard.player1, scoreboard.l_score)
            # if is_paused == False or game_is_On == False:
            #     final_time = elapsed_time
            #     print(f"Final TIme: {final_time}")
            # Final.penup()
            # Final.color("red")
            # Final.goto(0, -60)
            # Final.clear()
            # Final.write(f"Game Ended in: {final_time}", False, align="center", font=("courier", 18, "bold"))
            # Final.hideturtle()


        if scoreboard.r_score >= win_score:
            # game_is_On = False
            is_paused = False
            music.play_Winning_Sound()
            Scoreboard.game_over(ball, scoreboard.player2, scoreboard.r_score)
            # if is_paused == False or game_is_On == False:
            #     final_time = elapsed_time
            #     print(f"Final TIme: {final_time}")
            # Final.penup()
            # Final.color("red")
            # Final.goto(0, -60)
            # Final.clear()
            # Final.write(f"Game Ended in: {final_time}", False, align="center", font=("courier", 18, "bold"))
            # Final.hideturtle()



        # game_is_On = False
    else:
        screen.update()
