import time
import turtle
from turtle import Screen, Turtle
import player1
import player2
from car_manager import CarManager
from scoreboard import Scoreboard


def road():
    pen = turtle.Turtle()
    pen.speed(0)
    #pen.right(90)
    pen.color("grey")
    pen.up()
    pen.goto(-300, 50)
    pen.pensize(30)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, -100)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 150)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 200)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.hideturtle()

    """pen.speed(0)
    # pen.right(90)
    pen.color("grey")
    pen.up()
    pen.goto(-300, -125)
    pen.pensize(30)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, -75)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 0)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 75)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 140)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300, 190)
    pen.down()
    pen.forward(600)
    pen.hideturtle()"""


screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("bg.gif")
player1 = player1.Player()
player2 = player2.Player()
scoreboard = Scoreboard()
screen.addshape("car_sprite2.gif")
screen.update()
road()
screen.update()
car_manager = CarManager()
screen.update()
screen.tracer(0)


screen.listen()
screen.onkey(player1.go_up, "w")
screen.onkey(player1.go_down, "s")
screen.onkey(player1.go_left, "a")
screen.onkey(player1.go_right, "d")
screen.onkey(player2.go_up, "Up")
screen.onkey(player2.go_down, "Down")
screen.onkey(player2.go_left, "Left")
screen.onkey(player2.go_right, "Right")

game_is_on = True
while game_is_on:

    if scoreboard.level > 3:
        scoreboard.level = 3
        scoreboard.update_scoreboard()
        scoreboard.game_over()
        game_is_on = False

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            scoreboard.y += 1
            scoreboard.increase_level()
            player1.go_to_start()
            player2.go_to_start()
            car_manager.level_up()
        if car.distance(player2) < 20:
            scoreboard.x += 1
            scoreboard.increase_level()
            player1.go_to_start()
            player2.go_to_start()
            car_manager.level_up()

    #Detect successful crossing
    if player1.is_at_finish_line():
        scoreboard.x += 1
        player1.go_to_start()
        player2.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    if player2.is_at_finish_line():
        scoreboard.y += 1
        player1.go_to_start()
        player2.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
