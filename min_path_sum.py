# PROBLEM STATEMENT
# =================
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.


# SOLUTION
# ========
# this is an implementation of minimum path sum. the way it works is based on a
# simple observation:
#
# 	current_min_path_sum = (current_value +
# 												 min(left_min_path_sum, above_min_path_sum))
#
# we use dynamic programming technique to avoid computing the same value
# multiple times. time complexity of this implementation is O(row x col)
def min_path_sum(grid):
    # memory for dynamic programming. this saves us from compiting the sum that
    # has already been computed
    memory = [[(None, None)] * len(r) for r in grid]
    import math

    # this is the core of the implementation. to find the minimum sum of the
    # current cell, we choose the smaller of minimum sum the left one or the
    # one above it
    def min_sum_for(row, col):
        # if we can find the answer in the memory, immediately return it
        mem_sum, mem_path = memory[row][col]
        if mem_sum is not None:
            return mem_sum, mem_path

        # if we have to compute it, see if its the top-left cell of the grid.
        # if it is, it's just the value of the cell itself
        if row == 0 and col == 0:
            memory[row][col] = grid[row][col], [(row, col)]
            return memory[row][col]

        # otherwise, get the minimum sum of the left and above one. we then
        # choose the smaller one and add the current value of on top of it
        left_sum, left_path = min_sum_for(row, col - 1) if col > 0 else (math.inf, [])
        above_sum, above_path = min_sum_for(row - 1, col) if row > 0 else (math.inf, [])
        if left_sum < above_sum:
            memory[row][col] = grid[row][col] + left_sum, left_path + [(row, col)]
        else:
            memory[row][col] = grid[row][col] + above_sum, above_path + [(row, col)]
        return memory[row][col]

    # the rest of this function is to compute the minimum sum of the bottom right
    start_row = len(grid) - 1
    start_col = len(grid[start_row]) - 1
    return min_sum_for(start_row, start_col) + (memory,)


# helper function to print a grid
def print_grid(grid, indent="\t"):
    lines = (",".join(f"{v:5}" for v in row) for row in grid)
    for line in lines:
        print(f"{indent}{line}")


# helper function to test the implementation with data for inspection
def test(grid, show_memory=True):
    print("For grid:")
    print_grid(grid)

    sum, path, memory = min_path_sum(grid)
    print(f"Min path sum is: {sum}")

    print(f"Indices to get the sum:")
    for r, c in path:
        print(f"\t({r:3}, {c:3}) -> {grid[r][c]:5}")

    if show_memory:
        print("Here the memory:")
        only_sum = ((s for s, _ in row) for row in memory)
        print_grid(only_sum)


# here's the test input
grid = [
    [5, 9, 6, 8, 7],
    [3, 4, 2, 1, 9],
    [8, 7, 5, 3, 2],
    [6, 2, 4, 6, 8],
    [9, 3, 1, 2, 4],
]
test(grid)
