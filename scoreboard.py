from food import Food
from turtle import Turtle


class Scoree(Turtle):


    def __init__(self):
        super().__init__();
        self.score=0;
        self.hi_score=0;
        with open("hi_score.txt",mode="r") as file:
            self.hi_score=file.read();
        self.color("white")
        self.penup();
        self.goto(0,275)
        self.hideturtle();
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hi_score}", False, "center", ('Arial', 15, 'normal'))

    def track(self):
        self.clear();
        self.score=self.score+1;
        self.write(f"Score: {self.score} High Score: {self.hi_score}", False, "center", ('Arial', 15, 'normal'))


    def reset(self):
        with open("hi_score.txt",mode="r") as file:
            self.hi_score=int(file.read());
            if int(self.hi_score) <self.score:
                self.hi_score = self.score;
        with open("hi_score.txt",mode="w") as file:
            file.write(str(self.hi_score));

        self.score=0;
        self.update_score();
