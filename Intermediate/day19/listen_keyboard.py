import turtle

seemaan = turtle.Turtle()
screen = turtle.Screen()
seemaan.shape("turtle")
seemaan.turtlesize(0.8)


def move_forward():
    seemaan.forward(10)


def turn_left():
    seemaan.left(90)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="l", fun=turn_left)

screen.exitonclick()
