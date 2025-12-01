import time
from movement import clear, draw_grid
from grid import is_within_bounds, is_passable, grid  


def move_player(pos, action):
    x, y = pos
    if action == "w": x -= 1
    elif action == "s": x += 1
    elif action == "a": y -= 1
    elif action == "d": y += 1
    else:  # Invalid key
        return

    if is_within_bounds(grid, x, y) and is_passable(grid, x, y):
        pos[0], pos[1] = x, y
        # Check if new position is a lake
        if grid[x][y] == 2:
            print("\nEntering lake... (takes 2 turns)")
            time.sleep(1)  # simulate extra turn
            print("Leaving lake...\n")
            time.sleep(0.5)
# --- End of move_player ---

def show_legend():
    clear()
    print("=== LEGEND ===")
    print(". = Ground (1 turn)")
    print("~ = Lake (2 turns)")
    print("# = Mountain (blocked)")
    print("@ = Player")
    print("X = Goal")
    input("\nPress Enter to continue...")

def run_manual_mode():
    player_pos = [0, 0]
    goal_pos = [9, 9]

    show_legend()

    while player_pos != goal_pos:
        clear()
        draw_grid(player_pos, goal_pos)

        print("\nUse W/A/S/D to move, Q to quit")
        action = input("Move: ").lower()

        if action == "q":
            return

        move_player(player_pos, action)  

    print("\nYou've reached the goal\n")