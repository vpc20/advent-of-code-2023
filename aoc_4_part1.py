import re

from aoc_tools import read_input_to_text_array


def solve_part1():
    # input = read_input_to_text_array('aoc_4_test_data1.txt')
    input = read_input_to_text_array('aoc_4_data1.txt')
    rsplit_input = [line.rsplit(': ', maxsplit=2)[1] for line in input]

    all_numbers = [e.strip().split('|') for e in rsplit_input]
    total_points = 0
    for numbers in all_numbers:
        winning_numbers = set(re.findall(r'\d+', numbers[0]))
        my_numbers = re.findall(r'\d+', numbers[1])
        winning_num_count = len([my_number for my_number in my_numbers if my_number in winning_numbers])
        if winning_num_count > 0:
            total_points += 2 ** (winning_num_count - 1)
    return total_points


if __name__ == '__main__':
    print(solve_part1())
    # 527364
