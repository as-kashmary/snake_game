from turtle import Turtle

POSITION=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[];
        self.body();


    def body(self):
        for pos in POSITION:
            segment = Turtle("square");
            segment.color("white");
            segment.penup();
            segment.goto(pos);
            self.segments.append(segment);

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[num - 1].xcor();
            y = self.segments[num - 1].ycor();
            self.segments[num].goto(x, y);
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].seth(90)

    def down(self):
        self.segments[0].seth(270)

    def east(self):
        self.segments[0].seth(0)

    def west(self):
        self.segments[0].seth(180)