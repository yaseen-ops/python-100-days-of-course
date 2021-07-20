import turtle
import random

seemaan = turtle.Turtle()
turtle.colormode(255)
seemaan.shape("turtle")
seemaan.pensize(2)
seemaan.speed("fastest")
turtle.bgcolor("black")


# Creating random colors from colormode class
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):    # It will stop creating circles once it completed whole revolve
        seemaan.color(random_color())
        seemaan.circle(100)
        # seemaan.setheading(seemaan.heading() + 10)
        # OR
        seemaan.left(size_of_gap)


draw_spirograph(10)
seemaan.hideturtle()    # Hide the turtle after execution
my_screen = turtle.Screen()
my_screen.exitonclick()