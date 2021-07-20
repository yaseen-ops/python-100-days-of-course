from turtle import Turtle
MOVE_SPEED = 30


class Paddle:

    def __init__(self, position):
        # self.starting_position = (x_axis, y_axis)
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.turtlesize(stretch_len=1, stretch_wid=5)
        # self.paddle.goto(self.starting_position)
        # OR using "set position" instead of "goto"
        self.paddle.setposition(position)

    def go_up(self):
        y_position = self.paddle.ycor() + MOVE_SPEED
        self.paddle.goto(self.paddle.xcor(), y_position)

    def go_down(self):
        y_position = self.paddle.ycor() - MOVE_SPEED
        self.paddle.goto(self.paddle.xcor(), y_position)
