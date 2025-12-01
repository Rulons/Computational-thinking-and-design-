grid = [
    [0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 1, 1, 2, 0, 0, 1, 0, 2, 0],
    [0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 0, 0, 1, 0],
    [0, 2, 2, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 2, 0, 0],
    [2, 2, 0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 1, 0, 0]
]

def is_within_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def is_passable(grid, x, y):
    return grid[x][y] != 1

def movement_cost(grid, x, y):
    if grid[x][y] == 0: return 1
    if grid[x][y] == 2: return 2
    return float('inf')