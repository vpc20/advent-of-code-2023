import sys


def get_map_value(key, map_ranges):
    for map_range in map_ranges:
        lo = map_range[1]
        hi = map_range[1] + map_range[2] - 1
        if lo <= key <= hi:
            return map_range[0] + (key - lo)
    return key


def create_map_range(input_data):
    map_ranges_txt = [item for item in input_data.split('\n') if item[0].isdigit()]
    map_ranges_array = [item.split(' ') for item in map_ranges_txt]
    return [[int(e) for e in item] for item in map_ranges_array]


def parse_text_input():
    global input, seeds, array_of_map_ranges, i
    # f = open('aoc_5_test_data1.txt')
    f = open('aoc_5_data1.txt')
    input = f.read().split('\n\n')
    f.close()
    for e in input:
        print(e)
        print()
    seed_input = input[0]
    split_seed_input = seed_input.split(': ')
    seeds = [int(e) for e in split_seed_input[1].split()]
    print('-----seeds-----')
    print(seeds)
    print()

    print('-----array_of_map_ranges-----')
    array_of_map_ranges = []
    for i in range(1, len(input)):
        array_of_map_ranges.append(create_map_range(input[i]))
        print(array_of_map_ranges[-1])
    print()

    return seeds, array_of_map_ranges


if __name__ == '__main__':
    seeds, array_of_map_ranges = parse_text_input()

    min_location = sys.maxsize
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            seed = j
            print('seeds', seed, i)
            for k in range(len(array_of_map_ranges)):
                seed = get_map_value(seed, array_of_map_ranges[k])
            min_location = min(min_location, seed)

print(min_location)
# 226172555
