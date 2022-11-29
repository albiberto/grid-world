class State:
    def __init__(self, win_condition, lose_condition):
        self._win = win_condition
        self._lose = lose_condition

        self.position = (0, 0)

    @property
    def is_end(self):
        return self.position == self._win or self.position == self._lose

    def reward(self):
        if self.position == self._win:
            return 1
        elif self.position == self._lose:
            return -1
        else:
            return 0

    def next(self, action, deterministic):
        if deterministic:
            if action == "up":
                return self.position[0] - 1, self.position[1]
            elif action == "down":
                return self.position[0] + 1, self.position[1]
            elif action == "left":
                return self.position[0], self.position[1] - 1
            else:
                return self.position[0], self.position[1] + 1
