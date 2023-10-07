from turtle import Screen
from player import Player
from gameboard import GameBoard
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep

screen = Screen()
screen.setup(900, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()


player_1 = Player(-410)
player_2 = Player(410)
game_board = GameBoard()
ball = Ball()
scoreBoard_1 = ScoreBoard('left')
scoreBoard_2 = ScoreBoard('right')

on_game = True
while on_game:
    screen.onkey(player_1.move_up, 'w')
    screen.onkey(player_1.move_down, 's')
    screen.onkey(player_2.move_up, 'Up')
    screen.onkey(player_2.move_down, 'Down')
    # Paddle collisions
    sleep(0.01)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    
    if ball.xcor() < 0:
        for item in player_1.player:
            if ball.distance(item) < 40 and ball.xcor() <= -390:
                ball.bounce_x()
            elif ball.xcor() <= -450:
                scoreBoard_2.score_inc()
                ball.refresh()
    else:
        for item in player_2.player:
            if ball.distance(item) < 40 and ball.xcor() >= 390:
                ball.bounce_x()
            elif ball.xcor() >= 450:
                scoreBoard_1.score_inc()
                ball.refresh()
    
    
    

    screen.update()














screen.exitonclick()