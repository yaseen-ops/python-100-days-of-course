from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0 # Read the high score from the file
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.turtlesize(10)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()  # adding this score_update method
        self.score_update()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))   # OR data.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)

