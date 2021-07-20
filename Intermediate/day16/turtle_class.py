import turtle


def thambi_move():
    seemaan.forward(150)
    seemaan.left(90)


color_list = ["red", "blue", "brown", "green"]

seemaan = turtle.Turtle()
seemaan.shape("turtle")
seemaan.turtlesize(1.8)

for color in color_list:
    thambi_move()
    seemaan.color(color)


my_screen = turtle.Screen()
my_screen.exitonclick()