from turtle import Turtle

SNAKE_MOVEMENT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        turtle_object = Turtle("square")
        turtle_object.color("white")
        turtle_object.penup()
        x_cor = 0
        for _ in range(3):
            new_shape = turtle_object.clone()
            new_shape.goto(x_cor, 0)
            self.snake_body.append(new_shape)
            x_cor -= 20
        turtle_object.hideturtle()

    def add_segment(self):
        turtle_object = Turtle("square")
        turtle_object.color("white")
        turtle_object.penup()
        extended_part = turtle_object.clone()
        turtle_object.hideturtle()
        last_position = self.snake_body[-1].position()
        extended_part.goto(last_position)
        self.snake_body.append(extended_part)

    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[snake_part - 1].xcor()
            new_y_cor = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x_cor, new_y_cor)
        self.head.forward(SNAKE_MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
