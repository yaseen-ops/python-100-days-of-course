from turtle import Turtle, Screen
X_AXIS = -380
# Y_AXIS = (-250, -175, -100, -25, 50)
TURTLE_TYPES = ["red", "green", "purple", "black", "orange"]
screen = Screen()


class Race(Turtle):

    def __init__(self):
        super().__init__()
        self.all_turtles = []
        self.shape = "turtle"
        self.size = 0.8
        self.create_turtles()

    def create_turtles(self):
        y_axis = -250
        for create_turtle in TURTLE_TYPES:
            new_turtle = Turtle(shape=self.shape)
            new_turtle.penup()
            new_turtle.turtlesize = self.size
            new_turtle.color(create_turtle)
            new_turtle.goto(X_AXIS, y_axis)
            self.all_turtles.append(new_turtle)
            y_axis += 75

    # def move_turtle(self, move_forward):
    #     self.forward(move_forward)


class ScreenSetup:

    @staticmethod
    def screen_setup():
        screen.setup(width=800, height=600)

    @staticmethod
    def screen_exit():
        screen.exitonclick()


