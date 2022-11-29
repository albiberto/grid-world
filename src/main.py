from agent import Agent
from domain.board import Board
from domain.state import State

# global variables

BOARD_ROWS = 3
BOARD_COLUMNS = 4
OBSTACLES = [(1, 1), (1, 2)]
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START_STATE = (2, 0)
ROUNDS = 50
DETERMINISTIC = True


if __name__ == "__main__":
    board = Board(BOARD_ROWS, BOARD_COLUMNS, OBSTACLES)
    initial_state = State(WIN_STATE, LOSE_STATE)

    agent = Agent(board, initial_state, deterministic=DETERMINISTIC)
    agent.play(START_STATE, ROUNDS)

    print("Rewards grid:")
    agent.print()
