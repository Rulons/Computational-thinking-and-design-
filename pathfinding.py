# Grid definition
grid = [
    [0, 0, 0, 0, 0],  # Row 1
    [0, 1, 1, 0, 0],  # Row 2 (1s are obstacles)
    [0, 0, 0, 0, 0],  # Row 3
    [0, 1, 0, 1, 0],  # Row 4 (1s are obstacles)
    [0, 0, 0, 0, 0]   # Row 5
]

# Start and End points
start = (0, 0)  # Top-left corner
end = (4, 4)    # Bottom-right corner

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Function to check if a cell is within bounds
def is_within_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

# Function to check if a cell is passable (i.e., not an obstacle)
def is_passable(x, y, grid):
    return grid[x][y] == 0

# Testing: Print the grid
print("Initial Grid:")
print_grid(grid)

# Testing: Check if (2, 3) is within bounds and passable
x, y = 2, 3
print(f"Is ({x}, {y}) within bounds? {is_within_bounds(x, y, grid)}")
print(f"Is ({x}, {y}) passable? {is_passable(x, y, grid)}")