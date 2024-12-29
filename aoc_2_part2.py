from collections import defaultdict


def max_per_draw(item, max_possible):
    # max_count_dict = {'red': 12,
    #                   'green': 13,
    #                   'blue': 14,
    #                   }

    for e in item.split(', '):
        count_str, color = e.split(' ')
        # if int(count_str) <= max_count_dict[color]:
        #     max_possible[color] = max(max_possible[color], int(count_str))
        max_possible[color] = max(max_possible[color], int(count_str))


# part 1
# f = open('aoc_2_test_data1.txt')
f = open('aoc_2_data1.txt')

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
input = [line.strip().split(': ')[1:] for line in f]  # remove the 'Game n: ' prefix
# ['3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']

# for draws in input:
#     print(draws)
# print()
# temp2 = [re.findall(r'\d+ blue|\d+ red|\d+ green', line) for line in temp1]

game_sets = [e[0].split('; ') for e in input]
sum_id = 0
total_power = 0

for i, draws in enumerate(game_sets):
    print('draws in game_sets', draws)
    max_possible = defaultdict(int)
    for draw in draws:
        max_per_draw(draw, max_possible)
    total_power += max_possible['red'] * max_possible['green'] * max_possible['blue']

print(total_power)

f.close()
