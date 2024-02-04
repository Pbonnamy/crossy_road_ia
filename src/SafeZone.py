from src.Lane import Lane

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)

NUMBER_OF_OBSTACLES = [5, 6, 7, 8]


class SafeZone(Lane):
    def __init__(self, index, safe_type):
        super().__init__(index)
        self.safe_type = safe_type

    def get_color(self):
        return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2
