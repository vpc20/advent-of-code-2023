import re
from collections import defaultdict


def read_input_to_grid(in_file):
    f = open(in_file)
    result = [[c for c in line.strip()] for line in f]
    f.close()
    return result


def read_input_to_text_array(in_file):
    f = open(in_file)
    result = [line.strip() for line in f]
    f.close()
    return result


def read_input_to_list_of_grids(in_file):
    f = open(in_file)
    blocks = f.read().strip().split('\n\n')
    grids = []
    for block in blocks:
        rows = block.splitlines()
        grid = [list(row) for row in rows]
        grids.append(grid)
    f.close()
    return grids


def read_input_to_nums(in_file):
    f = open(in_file)
    nums = [re.findall(r'\d+', line) for line in f]
    result = [[int(n) for n in num] for num in nums]
    f.close()
    return result


def print_grid(arr):
    for e in arr:
        print(e)
    print()


def print_grid_with_tabs(arr):
    for e in arr:
        print(*e, sep='\t')
    print()


def print_grid_as_text(arr):
    for e in arr:
        print(''.join(c for c in e))
    print()


def create_graph_from_grid(grid):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    # if grid[r][c] == grid[nr][nc]:  # if grouped by same values in each cell
                    #     g[(r, c)].append((nr, nc))
                    # if grid[r][c] == grid[nr][nc]:  # if obstructions needs to be removed, e.g. maze problems
                    #     g[(r, c)].append((nr, nc))
                    g[(r, c)].append((nr, nc))
            else:
                _ = g[(r, c)]  # create empty list, use _ instead of dummy variable
    return g


if __name__ == '__main__':
    grid = read_input_to_grid('input.txt')
    print_grid(grid)
    print_grid_as_text(grid)

    x = read_input_to_nums('aoc_13_test_data1.txt')
    print(x)
    print_grid(x)

    x = read_input_to_nums('aoc_2_test_data1.txt')
    print_grid(x)
    print_grid_with_tabs(x)
