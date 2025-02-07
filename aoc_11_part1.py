from itertools import combinations

from aoc_tools import read_input_to_grid, create_graph_from_grid


def expand_rows(grid):
    new_grid = []
    ctr = 0
    for row in grid:
        if all(e == '.' for e in row):
            ctr += 1
            print(ctr)
            new_grid.append(row)
        new_grid.append(row)
    return new_grid


def expand_cols(grid):
    transposed_matrix = [list(row) for row in zip(*grid)]
    expanded_grid = expand_rows(transposed_matrix)
    return [list(row) for row in zip(*expanded_grid)]


def get_galaxy_pairs(grid):
    galaxy_coords, pairs = [], []
    nrows = len(grid)
    ncols = len(grid[0])

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == '#':
                galaxy_coords.append((r, c))

    return list(combinations(galaxy_coords, 2))


# the adjacency list (dictionary) contain only edges
# def dijkstra(g, src, tgt):
#     dists = {}  # distances
#     for vertex in g.keys():
#         dists[vertex] = sys.maxsize
#     dists[src] = 0
#     minq = [(0, src)]  # minimum priority queue
#
#     while minq:
#         estimate_dist, vertex = heappop(minq)
#         for neighbor in g[vertex]:  # breadth-first search
#             estimate_dist = dists[vertex] + 1
#             if estimate_dist < dists[neighbor]:  # relaxation
#                 dists[neighbor] = estimate_dist
#                 heappush(minq, (estimate_dist, neighbor))
#     return dists[tgt]

if __name__ == '__main__':
    grid = read_input_to_grid('aoc_11_data1.txt')
    # for e in grid:
    #     print(e)
    # print()

    grid = expand_cols(expand_rows(grid))
    # for e in grid:
    #     print(e)
    # print()
    # print_grid_as_text(grid)

    g = create_graph_from_grid(grid)
    # for k, v in g.items():
    #     print(k, v)

    sum_distances = 0
    galaxy_pairs = get_galaxy_pairs(grid)
    for coords1, coords2 in galaxy_pairs:
        dist = abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
        sum_distances += dist
        # sum_distances += dijkstra(g,pair[0], pair[1])
    print(sum_distances)
