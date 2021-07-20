import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")


game_is_on = True
INIT_LOOP = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # CREATE a CAR only when the loop runs for every 8 times to reduce the car accumulation
    # Either we can put similar condition in car_create() method in CarManager Class
    if INIT_LOOP == 8:
        car_manager.create_car()
        INIT_LOOP = 0
    INIT_LOOP += 1
    car_manager.move_cars()

    # Detect collision with CAR
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.reset_starting_position():
        car_manager.level_up()
        score_board.level_up()


screen.exitonclick()