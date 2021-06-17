from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep
screen = Screen()
Rpaddle = Paddle(350,0)
Lpaddle = Paddle(-350,0)
ball = Ball()
scoreboard = ScoreBoard()

screen.title('pong')
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(key='Up', fun=Rpaddle.up)
screen.onkey(key='Down', fun=Rpaddle.down)
screen.onkey(key='z', fun=Lpaddle.up)
screen.onkey(key='s', fun=Lpaddle.down)


game_on = True

while game_on:
    sleep(ball.move_speed) 
    ball.move()
    #********detect collition with the top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(Rpaddle) <50 and ball.xcor() >320 or ball.distance(Lpaddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        scoreboard.increase_Lscore()
        ball.reset()
        
    if ball.xcor() < -380:
        scoreboard.increase_Rscore()
        ball.reset()
    screen.update()







screen.exitonclick()
