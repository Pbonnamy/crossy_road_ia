import random

import arcade

from settings import SPRITE_SCALING, MAP_COL, SPRITE_SIZE, EMPTY, WALL
from src.Lane import Lane

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)

NUMBER_OF_OBSTACLES = [5, 6, 7, 8]


class Grass(Lane):

    def __init__(self, index):
        super().__init__(index)
        self.obstacles = arcade.SpriteList()

        for _ in range(random.choice(NUMBER_OF_OBSTACLES)):
            self.add_obstacle()

    def add_obstacle(self):
        obstacle_type = random.choice(['rock.png', 'cactus.png'])
        obstacle = arcade.Sprite(':resources:images/tiles/' + obstacle_type, SPRITE_SCALING)

        column = random.randint(0, MAP_COL - 1)
        obstacle.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
        obstacle.center_y = self.height / 2 + self.index * self.height

        while arcade.check_for_collision_with_list(obstacle, self.obstacles):
            column = random.randint(0, MAP_COL - 1)
            obstacle.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2

        self.obstacles.append(obstacle)

    def draw(self):
        # Draw lane
        super().draw()

        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw()

    def get_color(self):
        return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2

    def get_state(self, col):
        for obstacle in self.obstacles:
            if obstacle.center_x == col * SPRITE_SIZE + SPRITE_SIZE / 2:
                return WALL
        return EMPTY
