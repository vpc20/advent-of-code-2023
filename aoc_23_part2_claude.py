from collections import deque, defaultdict


def parse_map(filename):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows, cols = len(grid), len(grid[0])

    # Find start and end positions
    start = (0, grid[0].index('.'))
    end = (rows - 1, grid[rows - 1].index('.'))

    return grid, start, end


def build_graph(grid):
    """Build a graph representation where each non-forest tile is a node"""
    rows, cols = len(grid), len(grid[0])
    graph = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '#':  # If not a forest
                # For part 2, treat all slopes as regular paths
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        graph[(r, c)].append((nr, nc))

    return graph


def find_junctions(graph, start, end):
    """Find all junction nodes (nodes with more than 2 neighbors, or start/end)"""
    junctions = set()
    for node, neighbors in graph.items():
        if len(neighbors) > 2 or node == start or node == end:
            junctions.add(node)
    return junctions


def compress_graph(graph, junctions):
    """
    Create a compressed graph with only junction nodes.
    Edges represent paths between junctions with weights for path length.
    """
    compressed = defaultdict(list)

    for junction in junctions:
        # Find all junctions reachable from this junction
        queue = deque([(junction, 0)])
        visited = {junction}

        while queue:
            node, distance = queue.popleft()

            if node != junction and node in junctions:
                # Found another junction
                compressed[junction].append((node, distance))
                continue

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

    return compressed


def longest_path_dfs(graph, current, end, visited, current_length):
    """Use DFS to find the longest path without revisiting nodes"""
    if current == end:
        return current_length

    visited.add(current)
    max_length = 0

    for neighbor, weight in graph[current]:
        if neighbor not in visited:
            length = longest_path_dfs(graph, neighbor, end, visited.copy(), current_length + weight)
            max_length = max(max_length, length)

    return max_length


def main(filename):
    grid, start, end = parse_map(filename)

    # Build the full graph
    full_graph = build_graph(grid)

    # Find all junction nodes
    junctions = find_junctions(full_graph, start, end)

    # Create compressed graph with only junctions
    compressed_graph = compress_graph(full_graph, junctions)

    # Find the longest path using DFS
    longest = longest_path_dfs(compressed_graph, start, end, set(), 0)

    print(f"The longest hike is {longest} steps.")
    return longest


if __name__ == "__main__":
    # main("aoc_23_test_data1.txt")
    main("aoc_23_data1.txt")