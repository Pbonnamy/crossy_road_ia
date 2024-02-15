import arcade

from settings import MAP_COL, SPRITE_SIZE, MAP_ROW, SPRITE_SCALING, REWARD_WALL, REWARD_DEFAULT, UP_KEYS, DOWN_KEYS, LEFT_KEYS, RIGHT_KEYS, REWARD_GOAL, REWARD_CAR
from src.Agent import Agent
from src.Grass import Grass
from src.Road import Road


class Player:
    def __init__(self, lanes):
        self.sprite = arcade.Sprite(':resources:images/enemies/bee.png', SPRITE_SCALING)
        self.size = SPRITE_SIZE
        self.lanes = lanes
        self.agent = Agent(self, lanes)
        self.reset_position()

    def draw(self):
        self.sprite.draw()

    def reset_position(self):
        self.agent.score = 0
        self.sprite.center_x = MAP_COL * SPRITE_SIZE / 2
        self.sprite.center_y = SPRITE_SIZE / 2

    def move(self, key):
        center_x = self.sprite.center_x
        center_y = self.sprite.center_y

        if key in UP_KEYS:
            center_y += self.size
        elif key in DOWN_KEYS:
            center_y -= self.size
        elif key in LEFT_KEYS:
            center_x -= self.size
        elif key in RIGHT_KEYS:
            center_x += self.size

        if self.can_move(center_x, center_y):
            self.sprite.center_x = center_x
            self.sprite.center_y = center_y
            if self.current_row() == MAP_ROW - 1:
                return REWARD_GOAL
            else:
                for lane in self.lanes:
                    if lane.index == self.current_row() and isinstance(lane, Road):
                        if lane.hit_by_car(self):
                            return REWARD_CAR

            return REWARD_DEFAULT
        else:
            return REWARD_WALL

    def can_move(self, new_x, new_y):
        max_x = MAP_COL * SPRITE_SIZE
        max_y = MAP_ROW * SPRITE_SIZE

        # Check if the player is out of bounds
        if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
            return False

        target_row = int(new_y / self.size)

        # Check if the player is trying to move into an obstacle
        for lane in self.lanes:
            if lane.index == target_row and isinstance(lane, Grass):
                old_x, old_y = self.sprite.center_x, self.sprite.center_y
                self.sprite.center_x, self.sprite.center_y = new_x, new_y
                if arcade.check_for_collision_with_list(self.sprite, lane.obstacles):
                    self.sprite.center_x, self.sprite.center_y = old_x, old_y
                    return False
                break

        return True

    def current_row(self):
        return int(self.sprite.center_y / self.size)

    def current_col(self):
        return int(self.sprite.center_x / self.size)
