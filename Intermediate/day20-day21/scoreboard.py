from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.turtlesize(10)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)

