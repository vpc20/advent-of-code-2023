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
    elif card == 'J':
        return 1
    else:
        return int(card)


def get_strongest_hand_type(hand):
    strongest_hand_type = HIGH_CARD

    regular_cards = [c for c in hand if c != 'J']  # not Joker
    for c in regular_cards:
        replaced_hand = hand.replace('J', c)  # try replacing joker to make the stronges hand
        hand_set = set(list(replaced_hand))
        card_counter = Counter(replaced_hand)
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

        strongest_hand_type = max(strongest_hand_type, hand_type)

    return strongest_hand_type


def create_card_dict():
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
    input = read_input_to_text_array('aoc_7_test_data1.txt')
    # input = read_input_to_text_array('aoc_7_data1.txt')

    #  create card dictionary where hand type is key
    #  the dictionary consists of list of arranged card hands
    card_dict = create_card_dict()

    # sort the list of hands in ascending order
    card_dict = sort_hand_list(card_dict)
    # sort by hand type
    card_dict = dict(sorted(card_dict.items()))

    print(compute_total_winnings(card_dict))
