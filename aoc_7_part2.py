from collections import defaultdict, Counter
from itertools import product

from aoc_tools import read_input_to_text_array

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
    # elif card == 'J':  # in part 2,  J card are jokers
    #     return 11
    elif card == 'T':
        return 10
    elif card == 'J':
        return 1
    else:
        return int(card)


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

    return hand_type


def get_strongest_hand_type(hand):
    strongest_hand_type = HIGH_CARD
    strongest_hand = ''

    if hand == 'JJJJJ':
        return FIVE_OF_A_KIND

    if 'J' not in hand:
        return get_hand_type(hand)

    regular_cards = [c for c in hand if c != 'J']  # not Joker
    countj = hand.count('J')
    arr = [list(set(regular_cards)) for i in range(countj)]

    for p in product(*arr):
        print('p', p)
        permuted_hand = hand
        for c in p:
            permuted_hand = permuted_hand.replace('J', c, 1)
        print('hand, permuted_hand', hand, permuted_hand)
        new_hand_type = get_hand_type(permuted_hand)
        if new_hand_type > strongest_hand_type:
            strongest_hand_type = new_hand_type
            strongest_hand = permuted_hand

    return strongest_hand_type


def create_card_dict(input):
    card_dict = defaultdict(list)
    for e in input:
        hand, bid = e.split()
        hand_type = get_strongest_hand_type(hand)
        card_dict[hand_type].append((hand, int(bid)))
    return card_dict


def sort_hand_list(card_dict):
    for k, v in card_dict.items():
        sortedv = sorted(v, key=lambda e: (
            card_val(e[0][0]), card_val(e[0][1]), card_val(e[0][2]), card_val(e[0][3]), card_val(e[0][4])))
        card_dict[k] = sortedv
    return card_dict


def compute_total_winnings(card_dict):
    total_winnings, rank = 0, 0
    for hand_type, hand_list in card_dict.items():
        for card_hand, bid in hand_list:
            rank += 1
            print(hand_type, card_hand, bid, rank)
            total_winnings += bid * rank
    return total_winnings


if __name__ == '__main__':
    # input = read_input_to_text_array('aoc_7_test_data1.txt')
    # input = read_input_to_text_array('aoc_7_test_data2.txt')
    input = read_input_to_text_array('aoc_7_data1.txt')

    #  create card dictionary where hand type is key
    #  the dictionary consists of list of arranged card hands
    card_dict = create_card_dict(input)

    # sort the list of hands in ascending order
    card_dict = sort_hand_list(card_dict)
    # sort by hand type
    card_dict = dict(sorted(card_dict.items()))

    print(compute_total_winnings(card_dict))
    # 247885995

    # temp1 = [e.split()[0] for e in input]
    # print(temp1)
    # print(len(temp1))
    # print(len(set(temp1)))

