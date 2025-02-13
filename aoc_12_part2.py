import sys
from functools import cache


@cache
def count_arrangements(s, brokens, broken_ctr=0, arrangement=''):
    def count_helper(s, brokens, broken_ctr, arrangement):
        # print(s, brokens, broken_ctr)
        nonlocal count
        # if (s, brokens, broken_ctr) in set1:
        #     print('loop')
            # exit()
        # set1.add((s, brokens, broken_ctr))
        if s == '' and not brokens:
            count += 1
            # print(arrangement)
            return

        if s == '' and brokens:
            if len(brokens) == 1 and brokens[0] == broken_ctr:
                # print(arrangement)
                count += 1
            return

        if s[0] == '.':
            if not brokens:
                count_helper(s[1:].strip('.'), brokens, broken_ctr, arrangement + s[0])
            elif broken_ctr == brokens[0]:
                count_helper(s[1:].strip('.'), brokens[1:], 0, arrangement + s[0])
            else:
                if broken_ctr == 0:
                    count_helper(s[1:].strip('.'), brokens, broken_ctr, arrangement + s[0])
                else:
                    return
        elif s[0] == '#':
            if not brokens:
                return
            if brokens[0] == broken_ctr:
                return
            else:
                count_helper(s[1:], brokens, broken_ctr + 1, arrangement + s[0])
        elif s[0] == '?':
            count_helper(s.replace('?', '#', 1), brokens, broken_ctr, arrangement)
            count_helper(s.replace('?', '.', 1), brokens, broken_ctr, arrangement)

    print(s, brokens, broken_ctr)
    count = 0
    # set1 = set()
    count_helper(s, brokens, broken_ctr, arrangement)
    return count


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    f = open('aoc_12_test_data1.txt')
    input = [line.strip().split() for line in f]
    f.close()

    patterns = [item[0] for item in input]
    damages = [[int(e) for e in item[1].strip().split(',')] for item in input]

    sum_count = 0
    for i, pattern in enumerate(patterns):
        expanded_pattern = '?'.join(pattern for i in range(5))
        expanded_damages = damages[i] * 5
        sum_count += count_arrangements(expanded_pattern, tuple(expanded_damages))

    print(sum_count)
