from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_position()
        self.setheading(90)  # OR self.left(90)

    def start_position(self):
        self.setposition(STARTING_POSITION)

    # def move_turtle(self):
    #     y_position = self.ycor() + MOVE_DISTANCE
    #     self.goto(self.xcor(), y_position)

    # OR
    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def reset_starting_position(self):
        if self.ycor() == FINISH_LINE_Y:
            self.start_position()
            return True
        else:
            return False
