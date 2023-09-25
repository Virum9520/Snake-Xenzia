from turtle import Turtle, Screen
screen = Screen()

SPEED = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        x = 0
        for i in range(3):
            snake = Turtle()
            snake.shape('square')
            snake.color('blue')
            snake.penup()
            snake.setposition(x, 0)
            screen.update()
            x -= 20
            self.segments.append(snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(SPEED)

    def extend(self):
        snake = Turtle()
        snake.shape('square')
        snake.color('blue')
        snake.penup()
        snake.setposition(self.tail.pos())
        self.segments.append(snake)

    def reset_snake(self):
        self.segments.clear()
        self.create_snake()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
