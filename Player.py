import arcade

Z_KEY = 122
S_KEY = 115
Q_KEY = 113
D_KEY = 100


class Player:
    def __init__(self, scale, size, x, y):
        self.sprite = arcade.Sprite(':resources:images/enemies/bee.png', scale)
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.size = size

    def draw(self):
        self.sprite.draw()

    def move(self, key, max_x, max_y):
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

        if self.can_move(center_x, center_y, max_x, max_y):
            self.sprite.center_x = center_x
            self.sprite.center_y = center_y

    def can_move(self, new_x, new_y, max_x, max_y):
        return 0 <= new_x < max_x and 0 <= new_y < max_y
