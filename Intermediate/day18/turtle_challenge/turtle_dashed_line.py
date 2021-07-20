from turtle import Turtle, Screen

seemaan = Turtle()
seemaan.shape("turtle")
seemaan.turtlesize(.8)


def move_in_dashed_line(pace):
    seemaan.forward(pace)
    seemaan.penup()
    seemaan.forward(pace)
    seemaan.pendown()


for _ in range(15):
    move_in_dashed_line(pace=10)


my_screen = Screen()
my_screen.exitonclick()