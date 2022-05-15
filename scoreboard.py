from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.x = 0
        self.y = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}             {self.x} : {self.y}", align="left", font=FONT)
        return

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):

        if self.x > self.y:
            winner = "PLAYER 1"
        else:
            winner = "PLAYER 2"

        self.goto(0, 0)
        self.write(f"GAME OVER\n{winner} WINS\nPLAY AGAIN?\nY / N", align="center", font=FONT)

