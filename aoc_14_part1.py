from collections import defaultdict
from heapq import heappush, heappop

from aoc_tools import read_input_to_grid


def tilt_grid(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    tilted_grid = grid.copy()
    total_load = 0

    d1 = defaultdict(list)
    for j in range(ncols):
        if tilted_grid[0][j] == '.':
            heappush(d1[j], 0)
        elif tilted_grid[0][j] == 'O':
            total_load += nrows
    for k, v in d1.items():
        print(k, v)

    for i in range(1, nrows):
        for j in range(ncols):
            if tilted_grid[i][j] == '.':
                heappush(d1[j], i)
            elif tilted_grid[i][j] == '#':
                d1[j] = []
            elif tilted_grid[i][j] == 'O':
                if d1[j]:
                    mini = heappop(d1[j])
                    tilted_grid[i][j], tilted_grid[mini][j] = tilted_grid[mini][j], tilted_grid[i][j]
                    heappush(d1[j], i)
                    total_load += nrows - mini
                else:
                    total_load += nrows - i
    print(total_load)
    return tilted_grid


def compute_load(tilted_grid):
    total_load = 0
    return total_load


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_14_test_data1.txt')
    grid = read_input_to_grid('aoc_14_data1.txt')
    tilted_grid = tilt_grid(grid)
    for e in tilted_grid:
        print(e)
    # print(compute_load(tilted_grid))
