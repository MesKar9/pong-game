from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'bold')

class GameBoard:
    def __init__(self):
        self.center_ycor = 295
        self.center_lines = []
        self.center_lines_method()
    
    def center_lines_method(self):
        for i in range(0, 60):
            self.center_line = Turtle()
            if i % 2 == 0:
                self.center_line.color('white')
            else:
                self.center_line.color('black')
            self.center_line.penup()
            self.center_line.shape('square')
            self.center_line.shapesize(stretch_wid=0.1 , stretch_len=0.5)
            self.center_line.setpos(0, self.center_ycor)
            self.center_lines.append(self.center_line)
            self.center_ycor -= 10
    