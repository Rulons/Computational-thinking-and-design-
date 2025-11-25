import os
import random

# Player starting position
player_pos = [0, 0]

# Symbols:
# . = ground (normal)
# # = mountain (impassable)
# ~ = lake (requires 2 turns to enter)
# @ = player
# X = goal

# Terrain encoding
# 0 = ground
# 1 = mountain (impassable)
# 2 = lake (cost 2 moves)
# 3 = goal

GRID_SIZE = 10  # Grid size (10x10)

# Generate a grid with mountains and lakes
grid = []
for row_index in range(GRID_SIZE):
    row = []
    for col_index in range(GRID_SIZE):
        if row_index == GRID_SIZE - 1 and col_index == GRID_SIZE - 1:
            row.append(3)  # Goal in bottom-right
        else:
            # Randomly place mountains (~20%) or lakes (~15%), else ground
            chance = random.random()
            if chance < 0.2:
                row.append(1)  # Mountain
            elif chance < 0.35:
                row.append(2)  # Lake
            else:
                row.append(0)  # Ground
    grid.append(row)

# Track if waiting for lake
waiting_on_lake = False
lake_target = None  # position the user moves to

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw_grid(grid, player):
    for row_index in range(len(grid)):
        row_str = ""
        for col_index in range(len(grid[0])):
            if [row_index, col_index] == player:
                row_str += " @ "
            elif grid[row_index][col_index] == 1:
                row_str += " # "
            elif grid[row_index][col_index] == 2:
                row_str += " ~ "
            elif grid[row_index][col_index] == 3:
                row_str += " X "
            else:
                row_str += " . "
        print(row_str)

def move_player(direction):
    global waiting_on_lake, lake_target
    row, col = player_pos

    # If we are waiting on lake, move now
    if waiting_on_lake and lake_target is not None:
        player_pos[0], player_pos[1] = lake_target
        waiting_on_lake = False
        lake_target = None
        print("\nYou finish crossing the lake!")
        input("Press Enter to continue...")
        return

    # Determine new position
    if direction == "w":
        new_row, new_col = row - 1, col
    elif direction == "s":
        new_row, new_col = row + 1, col
    elif direction == "a":
        new_row, new_col = row, col - 1
    elif direction == "d":
        new_row, new_col = row, col + 1
    else:
        return  # invalid key

    # Check boundaries
    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
        print("\nYou can't move outside the map!")
        input("Press Enter to continue...")
        return

    # Check mountains
    if grid[new_row][new_col] == 1:
        print("\nA mountain blocks your way!")
        input("Press Enter to continue...")
        return

    # Check lake
    if grid[new_row][new_col] == 2:
        waiting_on_lake = True
        lake_target = [new_row, new_col]
        print("\nEntering lake... this takes extra effort")
        print("You must wait 1 turn before moving onto the lake.")
        input("Press Enter to continue...")
        return

    # Move player
    player_pos[0], player_pos[1] = new_row, new_col

    # Check if reached goal
    if grid[new_row][new_col] == 3:
        clear()
        draw_grid(grid, player_pos)
        print("\nCongratulations, you reached the goal!")
        exit()

# Legend and user guide
clear()
print("=== TERRAIN LEGEND ===")
print(". = Grass (normal ground, 1 turn)")
print("# = Mountain (impassable)")
print("~ = Lake (takes 2 turns to cross)")
print("@ = Player")
print("X = Goal")
print("\nUse W/A/S/D to move")
print("Press Q to quit\n")
input("Press Enter to start...")

while True:
    clear()
    draw_grid(grid, player_pos)

    print("\nW/A/S/D to move, Q to quit.")
    action = input("Move: ").lower()

    if action == "q":
        break

    move_player(action)