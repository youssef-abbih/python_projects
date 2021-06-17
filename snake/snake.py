from turtle import Turtle

POSITION = [(0,0),(-5,0),(-10,0)]
UP   = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
       
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]
    def create_snake(self):
        for index in POSITION:
            self.add_fragment(index)
    def add_fragment(self,index):
        snake = Turtle()
        snake.shape('square')
        snake.shapesize(stretch_len = 0.25,stretch_wid = 0.25)
        snake.color('black')
        snake.penup()
        snake.goto(index)
        self.snake_body.append(snake)
    def extend(self):
        self.add_fragment(self.tail.position())
    
    def move(self):
        for snake_index in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[snake_index-1].xcor()
            new_y = self.snake_body[snake_index-1].ycor()
            self.snake_body[snake_index].goto(new_x,new_y)
        self.head.fd(5)
    def reset(self):
        for fragment in self.snake_body:
            fragment.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.taim = self.snake_body[-1]

    def up(self):
       if self.head.heading() != DOWN:
           self.head.setheading(UP)
    def down(self):
       if self.head.heading() != UP:
           self.head.setheading(DOWN)
    def left(self):
       if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
    def right(self):
       if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

