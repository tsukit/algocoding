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
        pass

    for g in range(gen):
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = apply_rules(r, c)


def generate_grid(rows, cols):
    return [[bool(random.getrandbits(1)) for _ in range(cols)]
            for _ in range(rows)]


def test(grid, gen):
    print("initial state:")
    print_grid(grid)
    print(f"final state after {gen} generation(s)")
    print_grid(grid)


grid = generate_grid(5, 5)
test(grid, 1)

