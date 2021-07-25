from turtle import Turtle

ALIGNMENT = "center"
FONT = ("raleway", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        with open("data.txt", mode="r") as high_score_data:
            high_score = int(high_score_data.read())
        self.high_score = high_score
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.total_score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", mode="w") as high_score_data:
                high_score_data.write(f"{self.high_score}")
        self.total_score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.total_score += 1
        self.update_score()
