# PROBLEM STATEMENT
# Given a Binary Matrix mat[][] of order m*n. A cell with a value of zero
# is a Dead Cell, while a cell with a value of one is a Live Cell. The
# state of cells in a matrix mat[][] is known as Generation. The task is
# to find the next generation of cells based on the following rules:
#
# Any live cell with fewer than two live (< 2) neighbours dies as if caused
# by underpopulation.
#
# Any live cell with two or three live (= 2 or 3) neighbours lives on to the
# next generation.
#
# Any live cell with more than three live (> 3) neighbours dies, as if by
# overpopulation.
#
# Any dead cell with exactly three live ( = 3) neighbours becomes a live
# cell, as if by reproduction.

import random
from utils import print_grid


def game_of_life(grid, gen):
    rows = len(grid)
    cols = len(grid[0])

    def apply_rules(row, col):
        live_neighbors_cnt = sum([
            # top-left
            grid[row - 1][col - 1] if row > 0 and col > 0 else 0,
            # above
            grid[row - 1][col] if row > 0 else 0,
            # top-right
            grid[row - 1][col + 1] if row > 0 and col < cols - 1 else 0,
            # left
            grid[row][col - 1] if col > 0 else 0,
            # right
            grid[row][col + 1] if col < cols - 1 else 0,
            # bottom-left
            grid[row + 1][col - 1] if row < rows - 1 and col > 0 else 0,
            # below
            grid[row + 1][col] if row < rows - 1 else 0,
            # bottom-right
            grid[row + 1][col + 1] if row < rows - 1 and col < cols - 1 else 0,
        ])
        cur_alive = grid[row][col]
        if cur_alive:
            return (live_neighbors_cnt >= 2 and live_neighbors_cnt <= 3)
        else:
            return live_neighbors_cnt == 3

    for g in range(gen):
        grid = [[apply_rules(r, c) for c in range(cols)] for r in range(rows)]
    return grid


def generate_grid(rows, cols):
    return [[random.getrandbits(1) for _ in range(cols)] for _ in range(rows)]


def test(grid, gen):
    print("initial state:")
    print_grid(grid)

    result = game_of_life(grid, gen)

    print(f"final state after {gen} generation(s)")
    print_grid(result)


# grid = generate_grid(5, 5)
grid = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
test(grid, 1)

