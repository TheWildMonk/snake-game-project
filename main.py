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

# User control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Run the game
end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)
    snake.move()











# Screen exit
screen.exitonclick()
