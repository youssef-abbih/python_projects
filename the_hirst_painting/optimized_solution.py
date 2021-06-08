import colorgram
import turtle
from turtle import *
from random import choice

tim = Turtle()
tim.up()
tim.shape('turtle')
tim.hideturtle()
tim.speed(0)
tim.goto(-300,-300)

screen = Screen()
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
n = 100
pos = -250
for i in range(1,n+1):
    tim.dot(20, choice(rgb_colors))
    tim.fd(50)
    if i % 10 == 0 :
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.goto(-300,pos) 
        tim.setheading(0)
        pos += 50




turtle.done()
screen.exitonclick()

