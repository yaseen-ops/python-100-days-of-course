import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)

x_axis = -380
y_axis = -210
turtle_types = ["red", "green", "purple", "black", "orange", "blue"]
all_turtles = []
is_game_on = False
user_bet = turtle.textinput(title="Make a bet", prompt="Which Turtle will win the race?: ")

for set_turtle in turtle_types:
    build_turtle = turtle.Turtle(shape="turtle")
    build_turtle.penup()
    build_turtle.color(set_turtle)
    build_turtle.goto(x=x_axis, y=y_axis)
    y_axis += 85
    all_turtles.append(build_turtle)

if user_bet:
    is_game_on = True
while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 380:   # 380 = (width size for screen / 2) - 20
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} Turtle is the winner")
            else:
                print(f"You've Lost! The {winning_color} Turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
