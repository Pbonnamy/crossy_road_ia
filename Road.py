import arcade

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)


class Road:
    def __init__(self, index, height, width):
        self.index = index
        self.height = height
        self.width = width

    def draw(self):
        color = GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2
        center_x = self.width / 2
        center_y = self.height / 2 + self.index * self.height
        width = self.width
        height = self.height

        arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
