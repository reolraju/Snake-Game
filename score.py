from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("highscore.txt") as file:
            new_highscore=int(file.read())
        self.highestscore=new_highscore
        self.penup()
        self.color("white")
        self.setpos(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score_count} High Score:{self.highestscore}", align="center",
                   font=("Arial", 18, "normal"))

    def reset(self):
        if self.score_count > self.highestscore:
            self.highestscore = self.score_count
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highestscore}")

        self.score_count = 0
        self.update_score()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 18, "normal"))

    def inc_score(self):
        self.score_count += 1
        self.update_score()
