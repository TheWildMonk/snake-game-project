from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Create snake object
snake = Snake()
food = Food()
score = Scoreboard()

# User control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Run the game
game_speed = 0.1
end_game = False
while not end_game:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score.increase_score()
        game_speed -= 0.005

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        end_game = True
        score.game_over()

    for each_seg in snake.snake_body:
        if snake.head == each_seg:
            pass
        elif snake.head.distance(each_seg) < 10:
            end_game = True
            score.game_over()











# Screen exit
screen.exitonclick()
