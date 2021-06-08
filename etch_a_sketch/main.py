import turtle
from turtle import *


tim = Turtle()
screen = Screen()




forwards          = lambda : tim.fd(10)
backwards         = lambda : tim.bk(10)
counter_clockwise = lambda : tim.left(10)
clockwise         = lambda : tim.right(10)
def clear(): 
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
