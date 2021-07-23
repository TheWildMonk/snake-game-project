from turtle import Screen
from snake import Snake
import time

# Screen object definition
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=500)
screen.tracer(0)

# Snake object definition
snake = Snake()
print(snake.snake_body)

end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)
    snake.move()















# Screen exit
screen.exitonclick()