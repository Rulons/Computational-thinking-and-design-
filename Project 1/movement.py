import os
import time
from grid import grid

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw_grid(player, goal, path=None):
    for x in range(len(grid)):
        row = ""
        for y in range(len(grid[0])):
            if [x, y] == player:
                row += " @ "
            elif [x, y] == goal:
                row += " X "
            elif grid[x][y] == 1:
                row += " # "
            elif grid[x][y] == 2:
                row += " ~ "
            elif path and [x, y] in path:
                row += " * "
            else:
                row += " . "
        print(row)

def animate_path(path, player_pos, goal_pos):
    for step in path:
        player_pos[0], player_pos[1] = step
        clear()
        draw_grid(player_pos, goal_pos)
        time.sleep(0.3)