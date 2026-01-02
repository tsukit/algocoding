# helper function to print a grid
def print_grid(grid, *, width=5, indent="\t"):
    lines = (",".join(f"{v:{width}}" for v in row) for row in grid)
    for line in lines:
        print(f"{indent}{line}")

