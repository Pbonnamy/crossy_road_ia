import arcade

from settings import SPRITE_SIZE, MAP_COL


class Lane:
    def __init__(self, index):
        self.index = index
        self.height = SPRITE_SIZE
        self.width = MAP_COL * SPRITE_SIZE

    def draw(self):
        color = self.get_color()
        center_x = self.width / 2
        center_y = self.height / 2 + self.index * self.height
        width = self.width
        height = self.height

        # Draw lane
        arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

    def get_color(self):
        return (0, 0, 0)  # Default color

    def update(self):
        pass
