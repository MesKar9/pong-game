from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.hideturtle()
        self.penup()
        self.color('white')
        self.xcor = None
        self.score_position()
        self.setpos(self.xcor, 270)
        self.score = 0
        self.write(f'{self.score}', False, ALIGNMENT, FONT)
    
    def score_inc(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', False, ALIGNMENT, FONT)
    
    def score_position(self):
        if self.direction == 'left':
            self.xcor = -30
        elif self.direction == 'right':
            self.xcor = 30
        print(self.xcor)
        return self.xcor
