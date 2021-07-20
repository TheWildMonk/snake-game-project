from turtle import Turtle, Screen
import time

# Screen attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Turtle attributes
tim = Turtle()
tim.shape("square")
tim.color("white")
tim.penup()

# Generating snake body
snake_parts = []
x_cor = 0
for _ in range(3):
    new_shape = tim.clone()
    new_shape.goto(x_cor, 0)
    snake_parts.append(new_shape)
    x_cor -= 20

tim.hideturtle()

end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)
    for snake_part in range(len(snake_parts) - 1, 0, -1):
        new_x_cor = snake_parts[snake_part-1].xcor()
        new_y_cor = snake_parts[snake_part - 1].ycor()
        snake_parts[snake_part].goto(new_x_cor, new_y_cor)
    snake_parts[0].forward(20)
    snake_parts[0].left(90)












screen.exitonclick()
