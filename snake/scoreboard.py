from turtle import Turtle
import turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,220)
        self.ht()
        self.write(f"Score: {self.score}", align="center",font=("Verdana",20, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center",font=("Verdana",20, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center",font=("Verdana",20, "normal"))

