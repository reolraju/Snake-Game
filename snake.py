from turtle import Turtle

move_dist = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.RANGE = 3
        self.x = 0
        self.y = 0
        self.position = (self.x, self.y)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for s in range(self.RANGE):
            self.add_segment(self.position)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        self.segments.append(segment)
        self.x -= 20

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.RANGE = 3
        self.head = self.segments[0]

    def extend(self):
        self.RANGE += 1
        self.add_segment(self.segments[-1].position())

    def move(self):

        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].setpos(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
