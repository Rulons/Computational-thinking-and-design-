import heapq
from grid import is_within_bounds, is_passable, movement_cost

def get_neighbours(grid, x, y):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_within_bounds(grid, nx, ny) and is_passable(grid, nx, ny):
            yield (nx, ny)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def reconstruct_path(came_from, current):
    path = [list(current)]
    while current in came_from:
        current = came_from[current]
        path.append(list(current))
    return path[::-1]

def a_star(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbour in get_neighbours(grid, *current):
            tentative_g = g_score[current] + movement_cost(grid, *neighbour)

            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                f_score = tentative_g + heuristic(neighbour, goal)
                came_from[neighbour] = current
                heapq.heappush(open_set, (f_score, neighbour))

    return []