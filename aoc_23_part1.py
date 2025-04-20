import sys
from collections import defaultdict

from aoc_tools import read_input_to_grid


def create_graph(grid):
    # paths (.), forest (#), and steep slopes (^, >, v, and <)
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    # part 1
                    if grid[r][c] == '.' and grid[nr][nc] != '#' \
                            or grid[r][c] == '>' and grid[nr][nc] != '#' and nr == r and nc == c + 1 \
                            or grid[r][c] == '<' and grid[nr][nc] != '#' and nr == r and nc == c - 1 \
                            or grid[r][c] == '^' and grid[nr][nc] != '#' and nr == r - 1 and nc == c \
                            or grid[r][c] == 'v' and grid[nr][nc] != '#' and nr == r + 1 and nc == c:
                        g[(r, c)].append((nr, nc))
                    # part 2
                    # if grid[r][c] != '#' and grid[nr][nc] != '#':
                    #     g[(r, c)].append((nr, nc))
    return g


def hike_trail(g, start, end):
    def dfs(g, vertex, steps):
        nonlocal max_steps
        visited.add(vertex)
        # print(vertex, steps, end=' ')
        if vertex == end:
            print(f'hike finished: {steps} steps')
            max_steps = max(max_steps, steps)
            return
        for nb in g[vertex]:
            if nb not in visited:
                dfs(g, nb, steps + 1)
                visited.remove(nb)

    max_steps = 0
    visited = set()
    dfs(g, start, 0)
    print()
    return max_steps


if __name__ == '__main__':
    sys.setrecursionlimit(1000000000)

    grid = read_input_to_grid('aoc_23_data1.txt')
    # grid = read_input_to_grid('aoc_23_test_data1.txt')
    # grid = read_input_to_grid('aoc_23_test_data2.txt')
    # grid = read_input_to_grid('aoc_23_test_data3.txt')
    for e in grid:
        print(e)
    g = create_graph(grid)
    for k, v in g.items():
        print(k, v)

    start = (0, 1)
    nrows = len(grid)
    ncols = len(grid[0])
    end = (nrows - 1, ncols - 2)

    max_steps = hike_trail(g, start, end)
    print(f'max steps: {max_steps}')
