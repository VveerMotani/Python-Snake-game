import turtle as t
import time

x_pos = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:



    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for _ in range(3) :
            new_snake = t.Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x_pos[_])
            self.snakes.append(new_snake)
    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1) :
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVEDISTANCE)
        time.sleep(0.1)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)


    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(180)
