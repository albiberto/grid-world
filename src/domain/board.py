class Board:
    def __init__(self, right_bound, bottom_bound, obstacles):
        self._right_bound = right_bound
        self._bottom_bound = bottom_bound
        self._obstacles = obstacles

    @property
    def right_bound(self):
        return self._right_bound

    @property
    def bottom_bound(self):
        return self._bottom_bound

    @property
    def obstacles(self):
        return self._obstacles

    def print(self, current_position):

        for i in range(self.right_bound):
            print('------------------')
            out = '| '
            for j in range(self.bottom_bound):
                out += self.__get_value(current_position, i, j)
                out += ' | '
            print(out)

        print('------------------')

    def __get_value(self, position, i, j):

        if (i, j) == position:
            return '*'
        elif (i, j) in self.obstacles:
            return 'z'
        else:
            return '0'
