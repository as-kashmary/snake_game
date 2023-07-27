from turtle import Turtle,Screen
screen=Screen();
screen.setup(height=600,width=600);
screen.bgcolor("black")
screen.title("Snake Game")

position=[(0,0),(-20,0),(-40,0)]
for pos in position:
    segment=Turtle("square");
    segment.color("white");
    segment.goto(pos);




screen.exitonclick();