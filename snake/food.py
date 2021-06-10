from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len = 0.25, stretch_wid = 0.25)
        self.color('blue')
        self.speed(0)
        self.refresh()
    def refresh(self):
        self.goto(randint(-230,230),randint(-230,219))
