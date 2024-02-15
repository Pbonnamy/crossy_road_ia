import arcade
import random

from settings import SPRITE_SCALING, CAR_WIDTH, EMPTY, SPRITE_SIZE, CAR_RIGHT, CAR_LEFT, CAR_SPACINGS, CAR_SPEEDS
from src.Lane import Lane

ROAD_COLOR_1 = (82, 88, 102)
ROAD_COLOR_2 = (74, 80, 94)


class Road(Lane):
    def __init__(self, index, direction):
        super().__init__(index)
        self.cars = arcade.SpriteList()
        self.next_car_spacing = random.choice(CAR_SPACINGS)
        self.direction = direction
        self.car_speed = random.choice(CAR_SPEEDS) if self.direction == 'right' else -random.choice(CAR_SPEEDS)

    def add_car(self):
        car = arcade.Sprite('assets/car_' + self.direction + '.png', SPRITE_SCALING)

        if self.direction == 'right':
            car.center_x = -CAR_WIDTH / 2
        else:
            car.center_x = self.width + CAR_WIDTH / 2

        car.center_y = self.height / 2 + self.index * self.height
        self.cars.append(car)

    def hit_by_car(self, player):
        return arcade.check_for_collision_with_list(player.sprite, self.cars)

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

    def get_state(self, col):
        fake_player = arcade.Sprite(':resources:images/enemies/bee.png', SPRITE_SCALING)
        fake_player.center_x = col * SPRITE_SIZE + SPRITE_SIZE / 2
        fake_player.center_y = self.height / 2 + self.index * self.height
        for car in self.cars:
            if arcade.check_for_collision(fake_player, car):
                return CAR_RIGHT if self.direction == 'right' else CAR_LEFT
        return EMPTY
