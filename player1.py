from turtle import Turtle

STARTING_POSITION = (-100, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(2)
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.goto(self.pos()[0], self.pos()[1]+10)

    def go_down(self):
        self.goto(self.pos()[0], self.pos()[1]-10)

    def go_right(self):
        self.goto(self.pos()[0]+10, self.pos()[1])

    def go_left(self):
        self.goto(self.pos()[0]-10, self.pos()[1])

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
