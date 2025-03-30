import sys
from collections import deque

from aoc_tools import read_input_to_grid_int

# directions
NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

dir_dict = {NORTH: (WEST, EAST),
            EAST: (NORTH, SOUTH),
            SOUTH: (WEST, EAST),
            WEST: (NORTH, SOUTH),
            }


def map_traversal(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    pos = (0, 0)
    # end = (nrows - 1, ncols - 1)
    heat_loss = 0
    min_heat_loss = sys.maxsize

    q = deque()
    visited = set()
    for direction in (EAST, SOUTH):  # intial directions
        q.append((pos, direction, heat_loss))
        # visited.add((pos, direction))

    while q:
        pos, direction, heat_loss = q.popleft()
        r, c = pos
        if r == nrows - 1 and c == ncols - 1:  # lower right is the destination
            min_heat_loss = min(min_heat_loss, heat_loss)
            print('heat_loss ', heat_loss)
            continue
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))

        dr, dc = direction
        for _ in range(3):
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                for new_direction in dir_dict[direction]:
                    q.append(((nr, nc), new_direction, heat_loss + grid[nr][nc]))
    print(min_heat_loss)


if __name__ == '__main__':
    grid = read_input_to_grid_int('aoc_17_test_data1.txt')
    # grid = read_input_to_grid('aoc_17_data1.txt')

    for e in grid:
        print(e)

    map_traversal(grid)
