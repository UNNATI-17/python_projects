from turtle import Screen
import time
from day21_1 import Snake
from day21_3 import Scoreboard
from day21_2 import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreborad = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreborad.increase_score()
    if int(snake.head.xcor()) > 280 or int(snake.head.xcor()) < -280 or int(snake.head.ycor()) > 280 or int(snake.head.ycor()) < -280:  
        scoreborad.reset()
        snake.reset()
    for segment in snake.segment[1:]:
        if segment == snake.segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreborad.reset()
            snake.reset()
screen.exitonclick()