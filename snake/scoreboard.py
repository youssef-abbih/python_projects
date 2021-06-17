from turtle import Turtle
import turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0,220)
        self.ht()
        self.update()
    def increase_score(self):
        self.score += 1
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align="center",font=("Verdana",20, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center",font=("Verdana",20, "normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_high_score()
        self.score = 0
        self.update()
    def write_high_score(self):
        with open("data.txt",mode = "w") as data:
            data.write(f"{self.highscore}")

