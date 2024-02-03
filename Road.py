import arcade

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)

ROAD_COLOR_1 = (82, 88, 102)
ROAD_COLOR_2 = (74, 80, 94)


class Road:
    def __init__(self, road_type, index, height, width):
        self.road_type = road_type
        self.index = index
        self.height = height
        self.width = width

    def draw(self):
        color = self.get_color()
        center_x = self.width / 2
        center_y = self.height / 2 + self.index * self.height
        width = self.width
        height = self.height

        arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

    def get_color(self):
        match self.road_type:
            case 'road':
                return ROAD_COLOR_1 if self.index % 2 == 0 else ROAD_COLOR_2
            case 'grass':
                return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2

