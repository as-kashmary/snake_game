from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoree

screen=Screen();
screen.setup(height=600,width=600);
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake=Snake();
food=Food();
scor= Scoree();

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


    if snake.head.distance(food) <15:
        food.refresh();
        scor.track();
        snake.extend();

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        scor.reset();
        game_start=False;


    for s in snake.segments:
        if s== snake.head:
            pass;
        elif s.distance(snake.head) <10:
            scor.reset();
            game_start=False;

w=Turtle();
w.penup();
w.color("white");
w.write("GAME OVER",False,"center",("Ariel",15,"normal"));


screen.exitonclick();