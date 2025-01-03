from collections import defaultdict, Counter

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

    sorted_card_counter = dict(sorted(card_counter.items(), key=lambda e: (-e[1], -card_val(e[0]))))

    arranged_hand = ''
    for k, v in sorted_card_counter.items():
        arranged_hand += k * v

    return arranged_hand, hand_type


def create_card_dict():
    card_dict = defaultdict(list)
    for e in input:
        hand, bid = e.split()
        arranged_hand, hand_type = get_hand_type(hand)
        card_dict[hand_type].append((arranged_hand, int(bid)))
    return card_dict


def sort_card_hand_list(card_dict):
    for k, v in card_dict.items():
        sortedv = sorted(v, key=lambda e: (
            card_val(e[0][0]), card_val(e[0][1]), card_val(e[0][2]), card_val(e[0][3]), card_val(e[0][4])))
        card_dict[k] = sortedv
    return card_dict


def compute_total_winnings(card_dict):
    total_winnings, rank = 0, 0
    for k in sorted(card_dict.keys()):
        for card_hand, bid in card_dict[k]:
            rank += 1
            print(card_hand, bid, rank)
            total_winnings += bid * rank
    return total_winnings


if __name__ == '__main__':
    # input = read_input_to_text_array('aoc_7_test_data1.txt')
    input = read_input_to_text_array('aoc_7_data1.txt')

    #  create card dictionary where hand type is key
    #  the dictionary consists of list of arranged card hands
    card_dict = create_card_dict()

    # sort the list of card hands in ascending order
    card_dict = sort_card_hand_list(card_dict)

    print(compute_total_winnings(card_dict))

    # set1 = set()
    # for v in card_dict.values():
    #     for e in v:
    #         set1.add(e[0])
    # print(len(set1))
