import arcade
import random

from settings import SPRITE_SCALING, SPRITE_SIZE, MAP_COL, CAR_WIDTH
from src.Lane import Lane

ROAD_COLOR_1 = (82, 88, 102)
ROAD_COLOR_2 = (74, 80, 94)

CAR_SPEEDS = [2, 2.5, 3]

MIN_SPACING_BETWEEN_CARS = 1
MAX_SPACING_BETWEEN_CARS = 5


class Road(Lane):
    def __init__(self, index):
        super().__init__(index)
        self.cars = []
        self.next_car_spacing = random.randint(MIN_SPACING_BETWEEN_CARS, MAX_SPACING_BETWEEN_CARS)
        self.car_speed = random.choice(CAR_SPEEDS)

    def add_car(self):
        car = arcade.Sprite('assets/car_right.png', SPRITE_SCALING)
        car.center_x = -CAR_WIDTH / 2
        car.center_y = self.height / 2 + self.index * self.height
        self.cars.append(car)

    def update(self):
        # Handle car spawning
        if len(self.cars) == 0 or self.cars[-1].center_x - CAR_WIDTH / 2 > self.next_car_spacing * CAR_WIDTH:
            self.add_car()
            self.next_car_spacing = random.randint(MIN_SPACING_BETWEEN_CARS, MAX_SPACING_BETWEEN_CARS)

        # Handle car movement
        for car in self.cars:
            car.center_x += self.car_speed
            if car.center_x - CAR_WIDTH / 2 > self.width:
                self.cars.remove(car)

    def draw(self):
        # Draw lane
        super().draw()

        # Draw cars
        for car in self.cars:
            car.draw()

    def get_color(self):
        return ROAD_COLOR_1 if self.index % 2 == 0 else ROAD_COLOR_2
