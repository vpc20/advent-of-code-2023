import sys

from aoc_tools import read_input_to_grid


def find_start_pos(grid):
    # g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    found = False
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == 'S':
                start_row, start_col = r, c
                found = True
                break
        if found:
            break

    return (start_row, start_col)


def get_neighbors(grid, vertex):
    neighbors = []
    nrows = len(grid)
    ncols = len(grid[0])
    directions = {'F': [(0, 1), (1, 0)],
                  'L': [(0, 1), (-1, 0)],
                  '7': [(0, -1), (1, 0)],
                  'J': [(-1, 0), (0, -1)],
                  '-': [(0, -1), (0, 1)],
                  '|': [(-1, 0), (1, 0)],
                  'S': [(0, 1), (0, -1), (1, 0), (-1, 0)]
                  }

    r, c = vertex
    curr_char = grid[r][c]
    for direction in directions[curr_char]:
        dr, dc = direction
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols:
            next_char = grid[nr][nc]
            if ((direction == (0, 1) and next_char in '-J7')
                    or (direction == (0, -1) and next_char in '-LF')
                    or (direction == (1, 0) and next_char in '|JL')
                    or (direction == (-1, 0) and next_char in '|7F')):
                neighbors.append((nr, nc))
    return neighbors


def pipe_traversal(grid, start_coords):
    def dfs(grid, coords):
        visited.add(coords)
        print(coords, end=' ')
        for neighbor in get_neighbors(grid, coords):
            if neighbor not in visited:
                dfs(grid, neighbor)
        return len(visited) // 2

    visited = set()
    return dfs(grid, start_coords)
    # print()


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    grid = read_input_to_grid('aoc_10_data1.txt')
    for e in grid:
        print(e)

    start_coords = find_start_pos(grid)
    print(pipe_traversal(grid, start_coords))
