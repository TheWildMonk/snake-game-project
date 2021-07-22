from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

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

    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[snake_part - 1].xcor()
            new_y_cor = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x_cor, new_y_cor)
        self.snake_body[0].forward(20)
