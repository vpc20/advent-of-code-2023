from collections import deque

from aoc_tools import read_input_to_grid, print_grid_as_text

# directions
NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

dir_dict = {(NORTH, '/'): (EAST,),
            (EAST, '/'): (NORTH,),
            (SOUTH, '/'): (WEST,),
            (WEST, '/'): (SOUTH,),

            (NORTH, '\\'): (WEST,),
            (WEST, '\\'): (NORTH,),
            (SOUTH, '\\'): (EAST,),
            (EAST, '\\'): (SOUTH,),

            (NORTH, '-'): (EAST, WEST),
            (SOUTH, '-'): (EAST, WEST),

            (EAST, '|'): (NORTH, SOUTH),
            (WEST, '|'): (NORTH, SOUTH),

            }


def beam_traversal(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    pos = (0, 0)
    # direction = EAST # for test data
    direction = SOUTH

    q = deque()
    q.append((pos, direction))
    visited = set()

    while q:
        pos, direction = q.popleft()
        r, c = pos
        dr, dc = direction
        visited.add(((r, c), (dr, dc)))

        while True:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if ((nr, nc), (dr, dc)) in visited:
                    break
                visited.add(((nr, nc), (dr, dc)))
                if grid[nr][nc] in ('/', '\\'):
                    direction = dir_dict[(direction, grid[nr][nc])][0]
                    dr, dc = direction
                elif grid[nr][nc] == '-' or grid[nr][nc] == '|':
                    if (direction, grid[nr][nc]) in dir_dict:
                        direction1, direction2 = dir_dict[(direction, grid[nr][nc])]
                        q.append(((nr, nc), direction1))
                        q.append(((nr, nc), direction2))
                        break
                r, c = nr, nc
            else:
                break

    grid_copy = grid.copy()
    for pos, direction in visited:
        r, c = pos
        grid[r][c] = '#'

    for e in grid:
        print(e)
    print_grid_as_text(grid)

    print(len(visited))
    unique_pos = {pos for pos, direction in visited}
    print(len(unique_pos))


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_16_test_data1.txt')
    grid = read_input_to_grid('aoc_16_data1.txt')

    beam_traversal(grid)
