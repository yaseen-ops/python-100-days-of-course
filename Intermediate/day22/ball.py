from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(0.8)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def roam(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.goto(self.xcor() + 20, self.ycor() + 20)

    def bounce_yaxis(self):
        # when ball moves in (0 to +300) multiplying by '-' reverse the direction to (0 to -300)
        # when the ball moves in (0 to +300) multiplying by '-' reverse the direction to (0 to +300)
        # Simple logic - * + = - & - * - = +
        self.y_move *= -1

    def bounce_xaxis(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.setposition(0, 0)
        self.move_speed = 0.1  # Setting this to not to continue with last speed, but restart from initial speed
        # self.x_move *= -1
        # Since the method bounce_xaxis already using the above command
        self.bounce_xaxis()

