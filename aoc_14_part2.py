from collections import defaultdict
from heapq import heappush, heappop

from aoc_tools import read_input_to_grid


def rotate_clockwise(matrix):
    # Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    # Reverse each row to get the rotated matrix (flip vertically)
    rotated_matrix = [row[::-1] for row in transposed_matrix]
    return rotated_matrix


# def rotate_counter_clockwise(matrix):
#     Flip the matrix vertically
# flipped_vertival_matrix = [row[::-1] for row in matrix]
# Transpose to get the rotated matrix
# rotated_matrix = list(zip(*flipped_vertival_matrix))
#
# return rotated_matrix


def tilt_grid(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    tilted_grid = grid.copy()

    d1 = defaultdict(list)
    for j in range(ncols):
        if tilted_grid[0][j] == '.':
            heappush(d1[j], 0)
    # for k, v in d1.items():
    #     print(k, v)

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
    # print(total_load)
    return tilted_grid


def compute_load(grid):
    nrows = len(grid)
    # ncols = len(grid[0])
    total_load = 0
    for i, row in enumerate(grid):
        for e in row:
            if e == 'O':
                total_load += nrows - i
    return total_load


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_14_test_data1.txt')
    grid = read_input_to_grid('aoc_14_data1.txt')
    grid_orig = grid.copy()

    grid_set = set()
    grid_arr = [tuple(tuple(e) for e in grid)]
    for cycle in range(1, 1_000_000_001):
        for j in range(4):  # complete 1 cycle
            grid = tilt_grid(grid)
            grid = rotate_clockwise(grid)

        t1 = tuple(tuple(e) for e in grid)
        if t1 in grid_set:
            break
        grid_set.add(t1)
        grid_arr.append(t1)

    first = grid_arr.index(t1)
    # grid = grid_arr[(1_000_000_000 - first) % (cycle - first) + first]
    grid = grid_arr[(1_000_000_000 % (cycle - first)) + (cycle - first)]

    print(compute_load(grid))

    # 95736
