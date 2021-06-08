import turtle
from turtle import Turtle, Screen
from random import randint
turtle.bgcolor('black')
turtle.pensize(2)
turtle.shape('turtle')
turtle.speed('fastest')
screen = Screen()

screen.colormode(255)

def generator():
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    random_color =  (r,g,b)
    return random_color
for _ in range(36):
    turtle.color(generator())
    turtle.circle(100)
    turtle.left(10)


turtle.done()
screen.exitonclick()

