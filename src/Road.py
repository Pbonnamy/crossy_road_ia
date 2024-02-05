import arcade
import random

from settings import SPRITE_SCALING, CAR_WIDTH
from src.Lane import Lane

ROAD_COLOR_1 = (82, 88, 102)
ROAD_COLOR_2 = (74, 80, 94)

CAR_SPEEDS = [2, 2.5, 3]
CAR_SPACINGS = [1, 2, 3, 4, 5]


class Road(Lane):
    def __init__(self, index):
        super().__init__(index)
        self.cars = []
        self.next_car_spacing = random.choice(CAR_SPACINGS)
        self.direction = random.choice(['left', 'right'])
        self.car_speed = random.choice(CAR_SPEEDS) if self.direction == 'right' else -random.choice(CAR_SPEEDS)

    def add_car(self):
        car = arcade.Sprite('assets/car_' + self.direction + '.png', SPRITE_SCALING)

        if self.direction == 'right':
            car.center_x = -CAR_WIDTH / 2
        else:
            car.center_x = self.width + CAR_WIDTH / 2

        car.center_y = self.height / 2 + self.index * self.height
        self.cars.append(car)

    def update(self):
        # Handle car spawning
        if len(self.cars) == 0 or self.should_spawn():
            self.add_car()
            self.next_car_spacing = random.choice(CAR_SPACINGS)

        # Handle car movement
        for car in self.cars:
            car.center_x += self.car_speed
            if car.center_x - CAR_WIDTH / 2 > self.width or car.center_x + CAR_WIDTH / 2 < 0:
                self.cars.remove(car)

    def should_spawn(self):
        if self.direction == 'right':
            return self.cars[-1].center_x - CAR_WIDTH / 2 > self.next_car_spacing * CAR_WIDTH
        else:
            return self.cars[-1].center_x + CAR_WIDTH / 2 < self.width - self.next_car_spacing * CAR_WIDTH

    def draw(self):
        # Draw lane
        super().draw()

        # Draw cars
        for car in self.cars:
            car.draw()

    def get_color(self):
        return ROAD_COLOR_1 if self.index % 2 == 0 else ROAD_COLOR_2
