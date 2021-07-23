from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x_cor = 0
        snake_object = Turtle("square")
        snake_object.color("white")
        snake_object.penup()
        for _ in range(3):
            new_seg = snake_object.clone()
            new_seg.goto(x_cor, 0)
            x_cor -= 20
            self.snake_body.append(new_seg)
        snake_object.hideturtle()

    def move(self):
        for each_seg in range(len(self.snake_body) - 1, 0, 1):
            new_x_cor = self.snake_body[each_seg - 1].xcor()
            new_y_cor = self.snake_body[each_seg - 1].ycor()
            self.snake_body[each_seg].goto(new_x_cor, new_y_cor)
