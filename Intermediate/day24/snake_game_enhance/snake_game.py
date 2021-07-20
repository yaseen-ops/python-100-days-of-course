import time
from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard import Scoreboard


def control_snake():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
control_snake()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.13)
    snake.move()

    # Detect Snake collision with Food
    if snake.head.distance(food) < 15:
        # checking the distance between head of Snake and the food, since the food size is 10X10
        # Once the Snake goes near the food, the food should be recreated in some random position
        food.refresh()
        snake.extend_segment()
        score.increase_score()

    # Detect Snake collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # Checking if the snake hits wall with x & y axis, as the wall as built 600X600 which is X ( -300 to 300 )
        # & Y (-300 to 300 )
        # game_is_on = False
        # score.game_over()
        score.game_reset()
        snake.game_reset()

    # Detect Snake collision with its tail
    for segment in snake.segments[1:]:
        # Remove if statement and replacing with Slicing as [1:], refer slicing.py for details
        # # We need this first 'IF' check coz, the first segment is head which is
        # # segment = head and snake.head.distance(head) which will be same position and obviously less than "10"
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.game_reset()
            snake.game_reset()


screen.exitonclick()
