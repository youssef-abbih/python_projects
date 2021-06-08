from turtle import Turtle, Screen
import turtle
from random import choice,randint
timmy = Turtle()
screen = Screen()
timmy.color('blue', 'red')
timmy.shape('turtle')
timmy.width(15)
timmy.speed('fastest')
directions = [0,90,180,270]
screen.colormode(255)
def generator():
    r = randint(0,255) 
    b = randint(0,255)
    g = randint(0,255)
    random_color =  (r,g,b)
    return random_color
for i in range(1000):
    timmy.color(generator())
    timmy.forward(20)
    timmy.setheading(choice(directions))
    
turtle.done()
screen.exitonclick()                     
