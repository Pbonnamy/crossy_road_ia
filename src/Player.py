import arcade

from settings import MAP_COL, SPRITE_SIZE, MAP_ROW, SPRITE_SCALING

Z_KEY = 122
S_KEY = 115
Q_KEY = 113
D_KEY = 100


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

        if key == Z_KEY:
            center_y += self.size
        elif key == S_KEY:
            center_y -= self.size
        elif key == Q_KEY:
            center_x -= self.size
        elif key == D_KEY:
            center_x += self.size

        if self.can_move(center_x, center_y):
            self.sprite.center_x = center_x
            self.sprite.center_y = center_y

    def can_move(self, new_x, new_y):
        max_x = MAP_COL * SPRITE_SIZE
        max_y = MAP_ROW * SPRITE_SIZE
        return 0 <= new_x < max_x and 0 <= new_y < max_y
