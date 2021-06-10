import turtle
from turtle import *
from random import choice

colors =['red', 'blue', 'green', 'black']

y_position = [50, -50 ,-100, 100]

speed = list(range(0,10))

turtles = []

#******Screen****************************
screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgpic("race_road.png")
#******create the turtles****************
for turtle_index in range(0,4):
    tortuga= Turtle()
    tortuga.color(colors[turtle_index])
    tortuga.shape('turtle')
    tortuga.penup()
    tortuga.goto(-240,y_position[turtle_index])
    turtles.append(tortuga)

user_bet = screen.textinput(title = "Make your bet", prompt = "Wich turtle will win the race? ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        turtle.fd(choice(speed))

screen.exitonclick()
