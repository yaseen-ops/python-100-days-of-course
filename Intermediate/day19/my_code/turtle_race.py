import turtle
import random
from turtle_class import Race, ScreenSetup

ScreenSetup.screen_setup()

y_axis = -250
turtle_types = ["red", "green", "purple", "black", "orange"]
all_turtles = []
is_game_on = False
# user_bet = turtle.textinput(title="Make a bet", prompt="Which Turtle will win the race?: ")


race_turtle = Race()

# if user_bet:
#     is_game_on = True
# while is_game_on:
#
#     for turt in all_turtles:
#         print(turt.turtle_xcor())
#         if turt.turtle_xcor() > 230:
#             is_game_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've Won! The {winning_color} Turtle is the winner")
#             else:
#                 print(f"You've Lost! The {winning_color} Turtle is the winner")
#
#         random_distance = random.randint(0, 10)
#         turt.move_turtle(random_distance)

# x = 0
# while x > 10:
#     random_distance = random.randint(0, 10)
#     race_turtle.move_turtle(random_distance)
#     x += 1


ScreenSetup.screen_exit()