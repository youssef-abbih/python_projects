from turtle import *
from random import choice, randint
def generator():
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    return r,g,b

timmy = Turtle()
screen = Screen()
timmy.color('blue')
timmy.shape('turtle')
timmy.speed('fastest')
screen.colormode(255)
timmy.circle(100)







done()
screen.exitonclick()

