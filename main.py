from turtle import Turtle,Screen
import time
from snake import Snake

screen=Screen();
screen.setup(height=600,width=600);
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake=Snake();

screen.listen()

game_start=1;

while game_start:
    screen.update();
    time.sleep(0.09);
    snake.move();
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.east, "Right")
    screen.onkey(snake.west, "Left")


screen.exitonclick();