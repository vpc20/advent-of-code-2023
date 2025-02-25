from functools import cache


def parse_input(filename):
    """Parse the input file and return list of (pattern, groups) tuples."""
    result = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                pattern, groups = line.strip().split()
                groups = tuple(int(x) for x in groups.split(','))
                result.append((pattern, groups))
    return result


@cache
def count_arrangements(pattern: str, groups: tuple[int, ...], current_group: int = 0) -> int:
    """
    Recursively count valid arrangements using dynamic programming with memoization.

    Args:
        pattern: String of '.', '#', and '?' characters
        groups: Tuple of integers representing sizes of damaged spring groups
        current_group: Size of current group of damaged springs being processed

    Returns:
        Number of valid arrangements
    """
    # Base case: if pattern is empty
    if not pattern:
        # Valid if we've used all groups and not in middle of a group
        if not groups and current_group == 0:
            return 1
        # Valid if we're on last group and it matches current_group
        if len(groups) == 1 and groups[0] == current_group:
            return 1
        return 0

    result = 0
    possible_chars = ['#', '.'] if pattern[0] == '?' else [pattern[0]]

    for char in possible_chars:
        if char == '#':
            # Continue or start damaged group
            result += count_arrangements(pattern[1:], groups, current_group + 1)
        else:  # char == '.'
            if current_group == 0:
                # No group in progress, just move forward
                result += count_arrangements(pattern[1:], groups, 0)
            elif groups and groups[0] == current_group:
                # Successfully complete a group
                result += count_arrangements(pattern[1:], groups[1:], 0)

    return result


def solve_springs_puzzle(filename):
    """Solve the hot springs puzzle for the given input file."""
    records = parse_input(filename)
    total = 0

    for i, (pattern, groups) in enumerate(records, 1):
        expanded_pattern = '?'.join(pattern for i in range(5))
        expanded_groups = groups * 5
        arrangements = count_arrangements(expanded_pattern, expanded_groups)
        print(f"Row {i}: {pattern} {groups} -> {arrangements} arrangements")
        total += arrangements

    return total


if __name__ == "__main__":
    filename = "input.txt"  # Change this to match your input file name
    # filename = "aoc_12_data1.txt"  # Change this to match your input file name
    result = solve_springs_puzzle(filename)
    print(f"\nTotal arrangements: {result}")
