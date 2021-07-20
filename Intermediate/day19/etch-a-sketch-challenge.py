import turtle

seemaan = turtle.Turtle()
screen = turtle.Screen()
seemaan.shape("turtle")
seemaan.turtlesize(0.8)


def move_forward():
    seemaan.forward(10)


def move_backwards():
    seemaan.back(10)


def turn_left():
    seemaan.left(90)


def circle_clockwise():
    seemaan.circle(50, 50)


def circle_counter_clockwise():
    seemaan.circle(-50, 50)


def turn_left():
    seemaan.left(10)
    # # OR
    # new_heading = seemaan.heading() - 10
    # seemaan.setheading(new_heading)


def turn_right():
    seemaan.right(10)
    # # OR
    # new_heading = seemaan.heading() + 10
    # seemaan.setheading(new_heading)


def clear_screen():
    seemaan.reset()
    # # OR
    # seemaan.clear()
    # seemaan.penup()
    # seemaan.home()
    # seemaan.pendown()


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(circle_clockwise, "q")
screen.onkey(circle_counter_clockwise, "r")
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
