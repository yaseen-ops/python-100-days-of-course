from turtle import Turtle
MOVE_SPEED = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # Since inherited Turtle class, no need to use self.paddle.*
        # self.paddle = Turtle(shape="square")
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.setposition(position)

    def go_up(self):
        y_position = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), y_position)

    def go_down(self):
        y_position = self.ycor() - MOVE_SPEED
        self.goto(self.xcor(), y_position)
