from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
#******creating the objects****************************
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen = Screen()
#******Screen****************************
screen.title('Snake')
screen.setup(width = 500, height = 500)
screen.bgpic("snake.png")
screen.tracer(0)
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
        scoreboard.gameover()
        game_is_on = False
    for fragment in snake.snake_body[1:]:
        if snake.head.distance(fragment) < 4:
            game_is_on = False
            scoreboard.gameover()



screen.exitonclick()
