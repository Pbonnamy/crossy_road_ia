import random

from arcade.key import UP, LEFT, RIGHT


class BasicAgent:
    def __init__(self, player):
        self.player = player

    def choose_action(self, lanes):
        if self.player.can_move(self.player.sprite.center_x, self.player.sprite.center_y + self.player.size, lanes):
            return UP

        possible_moves = []

        if self.player.can_move(self.player.sprite.center_x - self.player.size, self.player.sprite.center_y, lanes):
            possible_moves.append(LEFT)
        if self.player.can_move(self.player.sprite.center_x + self.player.size, self.player.sprite.center_y, lanes):
            possible_moves.append(RIGHT)

        if possible_moves:
            return random.choice(possible_moves)

        return None

    def update(self, lanes):
        action = self.choose_action(lanes)
        if action is not None:
            self.player.move(action, lanes)
