from settings import SPRITE_SIZE, MAP_ROW, MAP_COL, WALL, ACTIONS


class Agent:
    def __init__(self, player, lanes):
        self.qtable = {}
        self.learning_rate = 1
        self.discount_factor = 1
        self.player = player
        self.lanes = lanes
        self.update()

    def update(self):
        current_state = self.get_state()
        print(current_state)
        self.add_state(current_state)

    def get_state(self):
        row = self.player.current_row() * SPRITE_SIZE
        col = self.player.current_col() * SPRITE_SIZE
        neighbors = [(row + SPRITE_SIZE, col - SPRITE_SIZE), (row + SPRITE_SIZE, col), (row + SPRITE_SIZE, col + SPRITE_SIZE),  # 0,0 - 0,1 - 0,2
                     (row, col - SPRITE_SIZE), (row, col + SPRITE_SIZE),  # 1,0 - 1,2 - (we don't need 1,1 because it's the player)
                     (row - SPRITE_SIZE, col - SPRITE_SIZE), (row - SPRITE_SIZE, col), (row - SPRITE_SIZE, col + SPRITE_SIZE)]  # 2,0 - 2,1 - 2,2

        state = []

        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= SPRITE_SIZE * MAP_ROW or neighbor[1] >= SPRITE_SIZE * MAP_COL:
                state.append(WALL)
            else:
                target_row = int(neighbor[0] / SPRITE_SIZE)
                target_col = int(neighbor[1] / SPRITE_SIZE)
                for lane in self.lanes:
                    if lane.index == target_row:
                        state.append(lane.get_state(target_col))
                        break

        return tuple(state)

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in ACTIONS:
                self.qtable[state][action] = 0.0
