import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
image = "Webp.net-gifmaker.gif"


class CarManager:

    def __init__(self):
        self.level = 1
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.pen = turtle.Turtle()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if self.level == 1:
            y = [-100, 50, 150, 200]
        elif self.level == 2:
            y = [-125, -75, 0, 75, 140, 190]
        else:
            y = [-150, -110, -65, -10, 50, 90, 125, 170, 210]

        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("car_sprite2.gif")
           # new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(y)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.level += 1
