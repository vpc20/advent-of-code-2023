from collections import defaultdict, Counter

from aoc_tools import read_input_to_text_array, print_text_array

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7


def card_val(card):
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    elif card == 'T':
        return 10
    else:
        return int(card)


def card_hand_val(v):
    card_hand_arr, bid = v
    total = 0
    for i, card in enumerate(card_hand_arr):
        total += card_val(card) * len(card_hand_arr) - i
    return total


def count_card_val(item):
    k, v = item
    pass


def get_hand_type(hand):
    hand_set = set(list(hand))
    card_counter = Counter(hand)
    if len(hand_set) == 5:
        hand_type = HIGH_CARD
    elif len(hand_set) == 4:
        hand_type = ONE_PAIR
    elif len(hand_set) == 3:
        if 3 in card_counter.values():
            hand_type = THREE_OF_A_KIND
        else:
            hand_type = TWO_PAIR
    elif len(hand_set) == 2:
        if 4 in card_counter.values():
            hand_type = FOUR_OF_A_KIND
        else:
            hand_type = FULL_HOUSE
    elif len(hand_set) == 1:
        hand_type = FIVE_OF_A_KIND

    # sorted_hand = sorted(list(hand), key=card_val, reverse=True)

    # x = sorted(card_counter, key=count_card_val, reverse=True)

    return sorted_hand, hand_type


def solve_part1():
    pass


if __name__ == '__main__':
    input = read_input_to_text_array('aoc_7_test_data1.txt')
    print(input)
    print_text_array(input)

    card_dict = defaultdict(list)
    for e in input:
        hand, bid = e.split()
        sorted_hand, hand_type = get_hand_type(hand)
        card_dict[hand_type].append((sorted_hand, int(bid)))

    for k, v in card_dict.items():
        print(v)
        sortedv = sorted(v, key=card_hand_val, reverse=True)
        card_dict[k] = sortedv

    for k, v in card_dict.items():
        print(k, v)
    print()

    total_winnings = 0
    rank = 0
    for k in sorted(card_dict.keys()):
        print(k)
        for card_hand, bid in card_dict[k]:
            print(card_hand)
            rank += 1
            print(bid, rank)
            total_winnings += bid * rank
    print(total_winnings)
