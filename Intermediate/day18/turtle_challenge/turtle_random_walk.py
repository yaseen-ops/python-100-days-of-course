import turtle
import random

seemaan = turtle.Turtle()
turtle.colormode(255)
seemaan.shape("turtle")


# Creating random colors from colormode class
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_created_color = (r, g, b)
    return random_created_color
    # OR  Simply
    # return r, g, b


# colors = ["red", "black", "green", "grey", "blue", "brown", "purple", "violet"]
directions = [0, 90, 180, 270]
seemaan.pensize(11)
seemaan.speed("fastest")
for _ in range(200):
    seemaan.color(random_color())
    seemaan.forward(25)
    seemaan.setheading(random.choice(directions))


my_screen = turtle.Screen()
my_screen.exitonclick()