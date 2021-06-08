import colorgram
import turtle
from turtle import *
from random import choice

tim = Turtle()
tim.up()
tim.shape('turtle')
tim.speed(1)
tim.goto(-100,-100)
print(tim.pos())
screen = Screen()
screen.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
n = 10
pos = -50
for i in range(n):
    for j in range(n):
        tim.dot(20, choice(rgb_colors))
        if j == n-1:
            tim.left(90)
        tim.fd(50)
    tim.goto(-100,pos)
    tim.setheading(0)
    pos += 50




turtle.done()
screen.exitonclick()

