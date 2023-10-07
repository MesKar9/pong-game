from turtle import Turtle



class Player:
    def __init__(self, xcor):
        self.player = []
        self.player_ycor = -60
        self.x_cor = xcor
        self.create_player()
    
    def create_player(self):
        for i in range(6):
            self.new_player = Turtle()
            self.new_player.color('white')
            self.new_player.shape('square')
            self.new_player.penup()
            self.new_player.setpos(self.x_cor, self.player_ycor)
            self.player.append(self.new_player)
            self.player_ycor += 20
    
    def move_up(self):
        for i in range(len(self.player)):
            self.turtle = self.player[i]
            self.turtle.setheading(90)
            self.turtle.forward(20)
        

    def move_down(self):
        for i in range(len(self.player)-1, -1, -1):
            self.turtle = self.player[i]
            self.turtle.setheading(270)
            self.turtle.forward(20)