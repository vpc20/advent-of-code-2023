def possible_draw(item):
    max_count_dict = {'red': 12,
                      'green': 13,
                      'blue': 14,
                      }

    x = item.split(', ')
    for e in x:
        count_str, color = e.split(' ')
        # print(count_str, color)
        if int(count_str) > max_count_dict[color]:
            return False
    return True


# part 1
# f = open('aoc_2_test_data1.txt')
f = open('aoc_2_data1.txt')

temp1 = [line.strip().split(': ')[1:] for line in f]  # remove the 'Game n: ' prefix
for e in temp1:
    print(e)
print()
# temp2 = [re.findall(r'\d+ blue|\d+ red|\d+ green', line) for line in temp1]

game_sets = [e[0].split('; ') for e in temp1]
sum_id = 0
for i, e in enumerate(game_sets):
    print('e in game_sets', e)
    for item in e:
        if not possible_draw(item):
            break
    else:
        sum_id += i + 1  # accumulate game id/no

print(sum_id)


f.close()
