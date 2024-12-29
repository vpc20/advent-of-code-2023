def possible_draw(item):
    max_count_dict = {'red': 12,
                      'green': 13,
                      'blue': 14,
                      }

    for e in item.split(', '):
        count_str, color = e.split(' ')
        if int(count_str) > max_count_dict[color]:
            return False
    return True


# part 1
f = open('aoc_2_test_data1.txt')
# f = open('aoc_2_data1.txt')

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
input = [line.strip().split(': ')[1:] for line in f]  # remove the 'Game n: ' prefix
# ['3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']

# for draws in input:
#     print(draws)
# print()
# temp2 = [re.findall(r'\d+ blue|\d+ red|\d+ green', line) for line in temp1]

game_sets = [e[0].split('; ') for e in input]
sum_id = 0
for i, draws in enumerate(game_sets):
    print('draws in game_sets', draws)
    for draw in draws:
        if not possible_draw(draw):
            break
    else:
        sum_id += i + 1  # accumulate game id/no

print(sum_id)


f.close()
