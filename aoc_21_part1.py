from collections import defaultdict, deque

from aoc_tools import read_input_to_grid


def create_graph(grid):
    # starting position(S), garden plots(.), and rocks(#)
    # starting position (S) also counts as a garden plot
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if grid[r][c] == 'S':
                        start = (r, c)
                    if grid[r][c] != '#' and grid[nr][nc] != '#':
                        g[(r, c)].append((nr, nc))
    return g, start


def navigate_gardens(g, grid, max_steps, start):
    q = deque()
    curr_step = 0
    q.append([(start), curr_step])

    while q:
        print(q)
        curr_node, curr_step = q.popleft()
        if curr_step == max_steps:
            break
        curr_step += 1
        for nb in g[curr_node]:
            r, c = nb
            grid[r][c] = curr_step
            if [nb, curr_step] not in q:
                q.append([nb, curr_step])

    for e in grid:
        print(e)

    step_ctr = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == max_steps:
                step_ctr += 1
    return step_ctr


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_21_test_data1.txt')
    grid = read_input_to_grid('aoc_21_data1.txt')
    for e in grid:
        print(e)
    g, start = create_graph(grid)
    for k, v in g.items():
        print(k, v)

    max_steps = 64
    step_ctr = navigate_gardens(g, grid, max_steps, start)
    print(step_ctr)
