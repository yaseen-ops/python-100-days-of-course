from turtle import Screen
from padle import Paddle


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
control_paddle()

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
