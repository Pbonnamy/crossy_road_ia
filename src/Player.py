import arcade

from settings import MAP_COL, SPRITE_SIZE, MAP_ROW, SPRITE_SCALING

UP_KEYS = [122, 65362]  # z, up arrow
DOWN_KEYS = [115, 65364]  # s, down arrow
LEFT_KEYS = [113, 65361]  # q, left arrow
RIGHT_KEYS = [100, 65363]  # d, right arrow


class Player:
    def __init__(self, x, y):
        self.sprite = arcade.Sprite(':resources:images/enemies/bee.png', SPRITE_SCALING)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.size = SPRITE_SIZE

    def draw(self):
        self.sprite.draw()

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

    def can_move(self, new_x, new_y):
        max_x = MAP_COL * SPRITE_SIZE
        max_y = MAP_ROW * SPRITE_SIZE
        return 0 <= new_x < max_x and 0 <= new_y < max_y
