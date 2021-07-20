from turtle import Turtle, Screen


def draw_square():
    seemaan.forward(150)
    seemaan.left(90)


color_list = ["red", "blue", "brown", "green"]

seemaan = Turtle()
seemaan.shape("turtle")
seemaan.turtlesize(1.8)

choose_color = 0
for _ in range(4):
    color = color_list[choose_color]
    draw_square()
    seemaan.color(color)
    choose_color += 1


my_screen = Screen()
my_screen.exitonclick()
