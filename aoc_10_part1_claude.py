from collections import deque


def read_input(filename):
    """Read the pipe maze from a text file."""
    with open(filename) as f:
        return [list(line.strip()) for line in f]


def find_start(grid):
    """Find the starting position 'S' in the grid."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return (i, j)
    return None


def get_connected_pipes(grid, pos):
    """Get all positions that are connected to the current position."""
    row, col = pos
    height, width = len(grid), len(grid[0])
    connected = []
    pipe = grid[row][col]

    # Define which directions each pipe type can connect to
    pipe_connections = {
        '|': [(1, 0), (-1, 0)],  # North and South
        '-': [(0, 1), (0, -1)],  # East and West
        'L': [(-1, 0), (0, 1)],  # North and East
        'J': [(-1, 0), (0, -1)],  # North and West
        '7': [(1, 0), (0, -1)],  # South and West
        'F': [(1, 0), (0, 1)],  # South and East
        'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]  # All directions for start
    }

    if pipe not in pipe_connections:
        return []

    for dx, dy in pipe_connections[pipe]:
        new_row, new_col = row + dx, col + dy

        # Check if position is within grid
        if 0 <= new_row < height and 0 <= new_col < width:
            next_pipe = grid[new_row][new_col]

            # Check if the pipes can connect
            if dx == 1 and next_pipe in '|LJ':  # Moving south
                connected.append((new_row, new_col))
            elif dx == -1 and next_pipe in '|7F':  # Moving north
                connected.append((new_row, new_col))
            elif dy == 1 and next_pipe in '-J7':  # Moving east
                connected.append((new_row, new_col))
            elif dy == -1 and next_pipe in '-LF':  # Moving west
                connected.append((new_row, new_col))

    return connected


def find_longest_path(grid):
    """Find the longest path in the loop from the starting position."""
    start = find_start(grid)
    if not start:
        return 0

    # Use BFS to find all distances
    distances = {start: 0}
    queue = deque([start])
    max_distance = 0

    while queue:
        current = queue.popleft()

        for next_pos in get_connected_pipes(grid, current):
            if next_pos not in distances:
                distances[next_pos] = distances[current] + 1
                max_distance = max(max_distance, distances[next_pos])
                queue.append(next_pos)

    return max_distance


def main():
    grid = read_input('input.txt')
    result = find_longest_path(grid)
    print(f"Steps to farthest point: {result}")


if __name__ == "__main__":
    main()