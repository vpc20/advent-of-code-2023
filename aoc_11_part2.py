from itertools import combinations

from aoc_tools import read_input_to_grid


def get_expanded_rows(grid):
    expanded_rows = []
    for i, row in enumerate(grid):
        if all(e == '.' for e in row):
            expanded_rows.append(i)
    return expanded_rows


def get_expanded_cols(grid):
    expanded_cols = []
    transposed_grid = [list(row) for row in zip(*grid)]
    return get_expanded_rows(transposed_grid)


# def expand_rows(grid):
#     new_grid = []
#     for row in grid:
#         if all(e == '.' for e in row):
#             new_grid.append(row)
#         new_grid.append(row)
#     return new_grid
#
#
# def expand_cols(grid):
#     transposed_matrix = [list(row) for row in zip(*grid)]
#     expanded_grid = expand_rows(transposed_matrix)
#     return [list(row) for row in zip(*expanded_grid)]


def get_galaxy_pairs(grid):
    galaxy_coords, pairs = [], []
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == '#':
                galaxy_coords.append((r, c))

    return list(combinations(galaxy_coords, 2))


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_11_test_data1.txt')
    grid = read_input_to_grid('aoc_11_data1.txt')
    # for e in grid:
    #     print(e)
    # print()

    # grid = expand_cols(expand_rows(grid))
    # for e in grid:
    #     print(e)
    # print()
    # print_grid_as_text(grid)

    # g = create_graph_from_grid(grid)
    # for k, v in g.items():
    #     print(k, v)

    expanded_rows = get_expanded_rows(grid)
    expanded_cols = get_expanded_cols(grid)
    print(expanded_rows)
    print(expanded_cols)

    sum_distances = 0
    galaxy_pairs = get_galaxy_pairs(grid)
    for coords1, coords2 in galaxy_pairs:
        dist = abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
        for row in expanded_rows:
            if coords1[0] < row < coords2[0] or coords2[0] < row < coords1[0]:
                dist += 999999  # 1_000_000 times expansion
        for col in expanded_cols:
            if coords1[1] < col < coords2[1] or coords2[1] < col < coords1[1]:
                dist += 999999  # 1_000_000 times expansion
        sum_distances += dist
        # sum_distances += dijkstra(g,pair[0], pair[1])
    print(sum_distances)
