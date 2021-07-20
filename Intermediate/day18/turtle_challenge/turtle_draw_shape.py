import turtle
import random

seemaan = turtle.Turtle()
seemaan.shape("turtle")
seemaan.turtlesize(0.8)

colors = ["red", "black", "green", "grey", "blue", "brown", "purple", "violet"]


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        seemaan.forward(50)
        seemaan.right(angle)


for shape in range(3, 11):
    seemaan.color(random.choice(colors))
    draw_shape(shape)


my_screen = turtle.Screen()
my_screen.exitonclick()