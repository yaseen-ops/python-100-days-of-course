from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360  # OR 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in STARTING_POSITIONS:
            """Create the Snake for the initial Game, use the add_segment method to add given segments"""
            # Below portion moved to add_segment method, since it requires to add a segment
            # everytime the snake eats the food. So we call the add_segment number of times per in this for loop
            # segment = Turtle(shape="square")
            # segment.color("white")
            # segment.penup()
            # segment.goto(position)
            # self.segments.append(segment)
            self.add_segment(position)

    def add_segment(self, position):
        """adds the segment"""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend_segment(self):
        """Grows the snake by one segment from the last segment everytime it takes food"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # self.segments[0].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

    def game_reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)    # To disappear the older snake
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def up(self):
        # If statements required because the Snake is now able to move backwards,
        # where in actual games Snake cannot move backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
