from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,X_POS,Y_POS):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(X_POS,Y_POS)
        self.seth(90)
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        #self.fd(20)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
