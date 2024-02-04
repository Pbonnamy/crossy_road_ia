from src.Lane import Lane

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)


class Grass(Lane):
    def get_color(self):
        return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2
