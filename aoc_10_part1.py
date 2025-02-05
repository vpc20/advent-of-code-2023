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
            g = update_graph(grid, g, r, c)
    return g, (srow, scol)


def update_graph(grid, g, r, c):
    nrows = len(grid)
    ncols = len(grid[0])

    if grid[r][c] == 'F':
        if 0 <= c + 1 < ncols and grid[r][c + 1] in ('-', '7', 'J'):
            g[(r, c)].append((r, c + 1))
        if 0 <= r + 1 < nrows and grid[r + 1][c] in ('|', 'L', 'J'):
            g[(r, c)].append((r + 1, c))
    elif grid[r][c] == 'L':
        if 0 <= c + 1 < ncols and grid[r][c + 1] in ('-', 'J', '7'):
            g[(r, c)].append((r, c + 1))
        if 0 <= r - 1 < nrows and grid[r - 1][c] in ('|', 'F', '7'):
            g[(r, c)].append((r - 1, c))
    elif grid[r][c] == '7':
        if 0 <= c - 1 < ncols and grid[r][c - 1] in ('-', 'F', 'L'):
            g[(r, c)].append((r, c - 1))
        if 0 <= r + 1 < nrows and grid[r + 1][c] in ('|', 'J', 'L'):
            g[(r, c)].append((r + 1, c))
    elif grid[r][c] == '-':
        if 0 <= c - 1 < ncols and grid[r][c - 1] in ('-', 'F', 'L'):
            g[(r, c)].append((r, c - 1))
        if 0 <= c + 1 < ncols and grid[r][c + 1] in ('-', '7', 'J'):
            g[(r, c)].append((r, c + 1))
    elif grid[r][c] == 'J':
        if 0 <= r - 1 < nrows and grid[r - 1][c] in ('|', '7', 'F'):
            g[(r, c)].append((r - 1, c))
        if 0 <= c - 1 < ncols and grid[r][c - 1] in ('-', 'L', 'F'):
            g[(r, c)].append((r, c - 1))
    elif grid[r][c] == '|':
        if 0 <= r - 1 < nrows and grid[r - 1][c] in ('|', 'F', '7'):
            g[(r, c)].append((r - 1, c))
        if 0 <= r + 1 < nrows and grid[r + 1][c] in ('|', 'L', 'J'):
            g[(r, c)].append((r + 1, c))

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
    grid = read_input_to_grid('aoc_10_test_data1.txt')
    for e in grid:
        print(e)

    g, scoords = create_graph(grid)
    for k, v in g.items():
        print(k, v)

    print(pipe_traversal(grid, g, scoords))
