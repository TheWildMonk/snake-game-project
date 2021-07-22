from turtle import Screen
from snake import Snake
import time

# Screen attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Create snake object
snake = Snake()

end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)
    snake.move()












screen.exitonclick()
