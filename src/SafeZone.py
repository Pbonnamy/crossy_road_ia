from settings import GOAL, EMPTY
from src.Lane import Lane

GRASS_COLOR_1 = (189, 244, 101)
GRASS_COLOR_2 = (181, 236, 93)


class SafeZone(Lane):

    def __init__(self, index, lane_type):
        super().__init__(index)
        self.lane_type = lane_type

    def get_color(self):
        return GRASS_COLOR_1 if self.index % 2 == 0 else GRASS_COLOR_2

    def get_state(self, col):
        return GOAL if self.lane_type == 'end' else EMPTY
