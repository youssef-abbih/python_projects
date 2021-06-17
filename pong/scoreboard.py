from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Lscore = 0
        self.Rscore = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(100,200)
        self.write(self.Rscore, align = 'center', font = ("courier", 80, "normal"))
        self.goto(-100,200)
        self.write(self.Lscore, align = 'center', font = ("courier", 80, "normal"))
    
    def increase_Lscore(self):
        self.Lscore += 1
        self.clear()
        self.update_scoreboard()
    def increase_Rscore(self):
        self.Rscore += 1
        self.clear()
        self.update_scoreboard()
