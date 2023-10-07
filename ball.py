from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = randint(1,10)
        self.y_move = randint(1,10)
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.home()