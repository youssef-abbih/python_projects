from turtle import Turtle, Screen
import turtle
timmy = Turtle()
screen = Screen()
timmy.color('blue', 'red')
timmy.shape('turtle')


def shape(face,color):
    timmy.color(color, 'red')
    angle = 360/face
    for _ in range(face):
        timmy.forward(100)
        timmy.right(angle)

shape(3,'blue')
shape(4,'red')
shape(5,'yellow')
shape(6,'orange')
shape(7,'green')
shape(8,'cyan')
shape(9,'black')
shape(10,'coral')
turtle.done()
screen.exitonclick()
