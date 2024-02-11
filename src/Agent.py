from settings import SPRITE_SIZE, MAP_ROW, MAP_COL, WALL, ACTIONS, ACTION_UP, UP_ARROW, ACTION_DOWN, DOWN_ARROW, \
    ACTION_LEFT, LEFT_ARROW, ACTION_RIGHT, RIGHT_ARROW, IDLE


def arg_max(table):
    return max(table, key=table.get)


class Agent:
    def __init__(self, player, lanes):
        self.qtable = {}
        self.learning_rate = 0.5
        self.discount_factor = 0.5
        self.player = player
        self.lanes = lanes
        self.score = 0
        self.state = self.get_state()
        self.add_state(self.state)

    def best_action(self):
        return arg_max(self.qtable[self.state])

    def get_key(self, action):
        if action == ACTION_UP:
            return UP_ARROW
        elif action == ACTION_DOWN:
            return DOWN_ARROW
        elif action == ACTION_LEFT:
            return LEFT_ARROW
        elif action == ACTION_RIGHT:
            return RIGHT_ARROW
        else:
            return IDLE

    def update(self):
        action = self.best_action()
        reward = self.player.move(self.get_key(action), self.lanes)
        self.score += reward
        new_state = self.get_state()
        self.add_state(new_state)

        max_q = max(self.qtable[new_state].values())
        delta = self.learning_rate * (reward + self.discount_factor * max_q - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state

    def get_state(self):
        row = self.player.current_row() * SPRITE_SIZE
        col = self.player.current_col() * SPRITE_SIZE
        neighbors = [
            (row + SPRITE_SIZE * 2, col - SPRITE_SIZE),
            (row + SPRITE_SIZE * 2, col),
            (row + SPRITE_SIZE * 2, col + SPRITE_SIZE),
            (row + SPRITE_SIZE * 3, col - SPRITE_SIZE),
            (row + SPRITE_SIZE * 3, col),
            (row + SPRITE_SIZE * 3, col + SPRITE_SIZE),
            (row + SPRITE_SIZE, col - SPRITE_SIZE),
            (row + SPRITE_SIZE, col),
            (row + SPRITE_SIZE, col + SPRITE_SIZE),
            (row, col - SPRITE_SIZE),
            (row, col - SPRITE_SIZE * 2),
            (row, col + SPRITE_SIZE),
            (row, col + SPRITE_SIZE * 2),
            (row - SPRITE_SIZE, col - SPRITE_SIZE),
            (row - SPRITE_SIZE, col - SPRITE_SIZE * 2),
            (row - SPRITE_SIZE, col),
            (row - SPRITE_SIZE, col + SPRITE_SIZE),
            (row - SPRITE_SIZE, col + SPRITE_SIZE * 2)
        ]

        state = []

        for neighbor in neighbors:
            if (
                neighbor[0] < 0
                or neighbor[1] < 0
                or neighbor[0] >= SPRITE_SIZE * MAP_ROW
                or neighbor[1] >= SPRITE_SIZE * MAP_COL
            ):
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
