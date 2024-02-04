import arcade
import random

from settings import SPRITE_SCALING, SPRITE_SIZE, MAP_COL, CAR_WIDTH

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)

ROAD_COLOR_1 = (82, 88, 102)
ROAD_COLOR_2 = (74, 80, 94)

CAR_SPEEDS = [2, 2.5, 3]

MIN_SPACING_BETWEEN_CARS = 1
MAX_SPACING_BETWEEN_CARS = 5


class Lane:
    def __init__(self, lane_type, index):
        self.lane_type = lane_type
        self.index = index
        self.height = SPRITE_SIZE
        self.width = MAP_COL * SPRITE_SIZE
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
        if self.lane_type == 'road':
            if len(self.cars) == 0 or self.cars[-1].center_x - CAR_WIDTH / 2 > self.next_car_spacing * CAR_WIDTH:
                self.add_car()
                self.next_car_spacing = random.randint(MIN_SPACING_BETWEEN_CARS, MAX_SPACING_BETWEEN_CARS)

        # Handle car movement
        for car in self.cars:
            car.center_x += self.car_speed
            if car.center_x - CAR_WIDTH / 2 > self.width:
                self.cars.remove(car)

    def draw(self):
        color = self.get_color()
        center_x = self.width / 2
        center_y = self.height / 2 + self.index * self.height
        width = self.width
        height = self.height

        # Draw lane
        arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

        # Draw cars
        for car in self.cars:
            car.draw()

    def get_color(self):
        match self.lane_type:
            case 'road':
                return ROAD_COLOR_1 if self.index % 2 == 0 else ROAD_COLOR_2
            case 'grass':
                return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2
