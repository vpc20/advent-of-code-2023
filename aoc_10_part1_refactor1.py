import sys
from collections import defaultdict

from aoc_tools import read_input_to_grid


def create_graph(grid):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == 'S':
                srow, scol = r, c
            elif grid[r][c] != '.':
                g = update_graph(grid, g, r, c)
    return g, (srow, scol)


def update_graph(grid, g, r, c):
    nrows = len(grid)
    ncols = len(grid[0])
    directions = {'F': [(0, 1), (1, 0)],
                  'L': [(0, 1), (-1, 0)],
                  '7': [(0, -1), (1, 0)],
                  'J': [(-1, 0), (0, -1)],
                  '-': [(0, -1), (0, 1)],
                  '|': [(-1, 0), (1, 0)]
                  }

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
                g[(r, c)].append((nr, nc))

    return g


def dfs(g, scoords):
    def _dfs(g, vertex):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in g[vertex]:
            if neighbor not in visited:
                _dfs(g, neighbor)
        return len(visited) // 2

    visited = set()
    return _dfs(g, scoords)
    # print()


def pipe_traversal(grid, g, scoords):
    for schar in ('F', '-', '7', '|', 'L', 'J'):
        srow, scol = scoords
        grid[srow][scol] = schar
        g = update_graph(grid, g, srow, scol)
        # print('pipe_traversal')
        # for k, v in g.items():
        #     print(k, v)
        return dfs(g, scoords)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    grid = read_input_to_grid('aoc_10_data1.txt')
    for e in grid:
        print(e)

    g, scoords = create_graph(grid)
    for k, v in g.items():
        print(k, v)

    print(pipe_traversal(grid, g, scoords))
