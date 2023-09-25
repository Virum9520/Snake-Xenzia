from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
scoreboard = Scoreboard()

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Snake touches food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Snake touches wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        scoreboard.reset_scoreboard()
        game_on = False

    # Snake touches body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            game_on = False

screen.exitonclick()
