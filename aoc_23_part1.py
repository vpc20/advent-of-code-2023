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
                    if grid[r][c] == '.' and grid[nr][nc] != '#' \
                            or grid[r][c] == '>' and grid[nr][nc] != '#' and nr == r and nc == c + 1 \
                            or grid[r][c] == '<' and grid[nr][nc] != '#' and nr == r and nc == c - 1 \
                            or grid[r][c] == '^' and grid[nr][nc] != '#' and nr == r - 1 and nc == c \
                            or grid[r][c] == 'v' and grid[nr][nc] != '#' and nr == r + 1 and nc == c:
                        g[(r, c)].append((nr, nc))
    return g


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_23_test_data1.txt')
    grid = read_input_to_grid('aoc_23_test_data1.txt')
    for e in grid:
        print(e)
    g = create_graph(grid)
    for k, v in g.items():
        print(k, v)

    # max_steps = 64
    # step_ctr = navigate_gardens(g, grid, max_steps, start)
    # print(step_ctr)
