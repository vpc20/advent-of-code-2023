import re

from aoc_tools import read_input_to_text_array


def solve_part1():
    # input = read_input_to_text_array('aoc_4_test_data1.txt')
    input = read_input_to_text_array('aoc_4_data1.txt')
    rsplit_input = [line.rsplit(': ', maxsplit=2)[1] for line in input]

    all_numbers = [e.strip().split('|') for e in rsplit_input]
    card_count_dict = {i: 1 for i in range(len(all_numbers))}
    print(card_count_dict)
    total_card_count = 0
    for i, numbers in enumerate(all_numbers):  # process each card
        print(numbers)
        winning_numbers = set(re.findall(r'\d+', numbers[0]))
        my_numbers = re.findall(r'\d+', numbers[1])
        for _ in range(card_count_dict[i]):  # repeat processing of cards based on the number of its copies
            winning_num_count = len([my_number for my_number in my_numbers if my_number in winning_numbers])
            for j in range(winning_num_count):
                card_count_dict[i + j + 1] += 1
        total_card_count += card_count_dict[i]
    return total_card_count


if __name__ == '__main__':
    print(solve_part1())
    # 5539496
