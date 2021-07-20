from turtle import Turtle
PACE = 10


class Divider(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pace = PACE
        self.color("white")
        self.penup()
        self.setposition(0, -280)
        self.left(90)
        self.pendown()
        self.create_dashed_line()

    def create_dashed_line(self):
        self.forward(self.pace)
        self.penup()
        self.forward(self.pace)
        self.pendown()
