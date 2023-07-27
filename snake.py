from turtle import Turtle

POSITION=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[];
        self.body();
        self.head=self.segments[0];

    def body(self):
        for pos in POSITION:
            self.add_seg(pos);
    def add_seg(self,pos):
        segment = Turtle("square");
        segment.color("white");
        segment.penup();
        segment.goto(pos);
        self.segments.append(segment);

    def extend(self):
        self.add_seg(self.segments[len(self.segments)-1].pos());



    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[num - 1].xcor();
            y = self.segments[num - 1].ycor();
            self.segments[num].goto(x, y);
        self.head.forward(20)

    def up(self):
        if self.head.heading() !=270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def east(self):
        if self.head.heading() !=180:
            self.head.seth(0)

    def west(self):
        if self.head.heading() != 0:
            self.head.seth(180)