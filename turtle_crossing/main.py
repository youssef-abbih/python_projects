import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key='Up', fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for i in car.cars:
    	if player.distance(i) < 20:
    		scoreboard.game_over()
    		game_is_on = False
    if player.ycor() == FINISH_LINE_Y:
    	player.reset()
    	scoreboard.increase_level()
    	car.increase_speed()          
screen.exitonclick()
