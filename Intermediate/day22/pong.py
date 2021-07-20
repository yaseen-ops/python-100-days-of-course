from turtle import Screen
from padle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from pong_court_divider import Divider


def control_paddle():
    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "e")
    screen.onkey(left_paddle.go_down, "d")


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()
control_paddle()
score = ScoreBoard()
divider = Divider()

# 300 = height of y axis from 0
# divider.pace = "PACE" or speed the turtle mentioned to move ( check in pong_court_divider.py)
screen_half_height = screen.window_height()//2
for _ in range(screen_half_height//divider.pace):
    divider.create_dashed_line()


game_on = True
while game_on:

    screen.update()
    # time.sleep(0.1)
    time.sleep(ball.move_speed)
    ball.roam()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_yaxis()

    # Detect Collision with Right Paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_xaxis()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.update_score("left")
    elif ball.xcor() < -380:
        ball.ball_reset()
        score.update_score("right")

screen.exitonclick()
