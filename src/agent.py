import numpy as np


class Agent:
    actions = ["up", "down", "left", "right"]

    def __init__(self, board, state, learning_rate=.2, exp_rate=.3, deterministic=True):
        self.board = board
        self.state = state
        self.learning_rate = learning_rate
        self.exp_rate = exp_rate
        self.learning_rate = learning_rate
        self._deterministic = deterministic

        self.states = []
        self.state_values = np.zeros([board.right_bound, board.bottom_bound])

    def print(self):
        for i in range(self.board.right_bound):
            print('----------------------------------')
            out = '| '
            for j in range(0, self.board.bottom_bound):
                out += str(self.state_values[(i, j)]).ljust(6)
                out += ' | '
            print(out)
        print('----------------------------------')

    def play(self, start, rounds=10):

        self.state.position = start
        self.board.print(start)

        index = 0
        while index < rounds:
            if self.state.is_end:
                self.board.print(self.state.position)
                print('----------------------------------')
                print('---------------END----------------')
                print('----------------------------------')

                index += 1
                self.__end(start)
            else:
                self.board.print(self.state.position)
                self.__continue()

    def __end(self, start):
        # back propagate
        reward = self.state.reward()

        # explicitly assign end state to reward values, for profiling purpose
        self.state_values[self.state.position] = reward

        for s in reversed(self.states):
            reward = self.state_values[s] + self.learning_rate * (reward - self.state_values[s])
            self.state_values[s] = round(reward, 3)

        self.states = []
        self.state.position = start

    def __continue(self):
        action = self.__choose_action()
        next_position = self.__valid_position(action)

        # trace states
        self.states.append(next_position)
        # update current state
        self.state.position = next_position

    def __choose_action(self):
        # choose action with most expected value
        max_next_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                # if the action is deterministic
                position = self.__valid_position(a)
                next_reward = self.state_values[position]
                if next_reward >= max_next_reward:
                    action = a
                    max_next_reward = next_reward

        return action

    def __valid_position(self, action):
        position = self.state.next(action, self._deterministic)

        in_board = 0 <= position[0] <= self.board.right_bound - 1 and 0 <= position[1] <= self.board.bottom_bound - 1
        return (self.state.position, position)[in_board and position not in self.board.obstacles]
