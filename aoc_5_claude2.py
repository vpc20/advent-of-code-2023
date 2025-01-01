from typing import List, Tuple


def parse_input(filename: str) -> tuple[List[Tuple[int, int]], List[List[Tuple[int, int, int]]]]:
    """
    Parse input file and return seed ranges and conversion maps.
    Returns:
        Tuple containing:
        - List of (start, length) tuples for seed ranges
        - List of mapping rules, where each rule is (destination_start, source_start, length)
    """
    with open(filename) as f:
        sections = f.read().strip().split('\n\n')

    # Parse seeds into ranges
    seed_numbers = [int(x) for x in sections[0].split(': ')[1].split()]
    seed_ranges = [(seed_numbers[i], seed_numbers[i + 1])
                   for i in range(0, len(seed_numbers), 2)]

    # Parse maps
    maps = []
    for section in sections[1:]:
        current_map = []
        for line in section.split('\n')[1:]:  # Skip the header line
            dest_start, src_start, length = map(int, line.split())
            current_map.append((dest_start, src_start, length))
        maps.append(current_map)

    return seed_ranges, maps


def process_range(input_range: Tuple[int, int],
                  mapping_rules: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    """
    Process a single range through a set of mapping rules.
    Args:
        input_range: Tuple of (start, length)
        mapping_rules: List of (destination_start, source_start, length) tuples
    Returns:
        List of transformed ranges as (start, length) tuples
    """
    start, length = input_range
    end = start + length
    ranges_to_process = [(start, end)]
    transformed_ranges = []

    for dest_start, src_start, rule_length in mapping_rules:
        src_end = src_start + rule_length
        offset = dest_start - src_start
        new_ranges_to_process = []

        while ranges_to_process:
            range_start, range_end = ranges_to_process.pop()

            # Split range into before, overlapping, and after portions
            before = (range_start, min(range_end, src_start))
            overlap = (max(range_start, src_start), min(range_end, src_end))
            after = (max(src_end, range_start), range_end)

            # Add non-empty ranges
            if before[1] > before[0]:
                new_ranges_to_process.append(before)
            if overlap[1] > overlap[0]:
                transformed_ranges.append((overlap[0] + offset, overlap[1] - overlap[0]))
            if after[1] > after[0]:
                new_ranges_to_process.append(after)

        ranges_to_process = new_ranges_to_process

    # Add any remaining untransformed ranges
    transformed_ranges.extend((start, end - start) for start, end in ranges_to_process)
    return transformed_ranges


def find_lowest_location(seed_ranges: List[Tuple[int, int]],
                         maps: List[List[Tuple[int, int, int]]]) -> int:
    """
    Find the lowest location number for any seed in the input ranges.
    Args:
        seed_ranges: List of (start, length) tuples representing seed ranges
        maps: List of mapping rules for each conversion step
    Returns:
        Lowest location number
    """
    current_ranges = seed_ranges

    # Process through each mapping level
    for mapping in maps:
        new_ranges = []
        for range_start, range_length in current_ranges:
            transformed = process_range((range_start, range_length), mapping)
            new_ranges.extend(transformed)
        current_ranges = new_ranges

    # Find the lowest start value from all final ranges
    return min(start for start, _ in current_ranges)


def main():
    # Parse input
    seed_ranges, maps = parse_input('aoc_5_test_data2.txt')

    # Find lowest location
    result = find_lowest_location(seed_ranges, maps)
    print(f"Lowest location number: {result}")


if __name__ == "__main__":
    main()
