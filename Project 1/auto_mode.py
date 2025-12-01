from pathfinding import a_star
from grid import grid
from movement import animate_path, clear, draw_grid

def run_auto_mode():
    player_pos = [0, 0]
    goal_pos = [9, 9]

    clear()
    draw_grid(player_pos, goal_pos)
    input("\nPress Enter to start A*...")

    path = a_star(grid, tuple(player_pos), tuple(goal_pos))

    if not path:
        print("No path found!")
        return

    animate_path(path[1:], player_pos, goal_pos)
    print("\nGoal reached!\n")