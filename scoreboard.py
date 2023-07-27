from food import Food
from turtle import Turtle


class Scoree(Turtle):


    def __init__(self):
        super().__init__();
        self.score=0;
        self.color("white")
        self.penup();
        self.goto(0,275)
        self.hideturtle();
        self.write(f"Score: {self.score}",False,"center",('Arial',15,'normal'))

    def track(self):
        self.clear();
        self.score=self.score+1;
        self.write(f"Score: {self.score}", False, "center", ('Arial', 15, 'normal'))