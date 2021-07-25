from turtle import Turtle

ALIGNMENT = "center"
FONT = ("raleway", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.high_score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"SCORE: {self.total_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.total_score += 1
        self.clear()
        self.update_score()