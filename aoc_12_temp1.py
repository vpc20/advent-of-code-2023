# for i in range(48):
#     print(52 + i, end=', ')

# list1 = [i for i in range(50, 98)]
# list2 = [i for i in range(52, 100)]
# print(list(zip(list1, list2)))

# for i in range(1_000_000):
#     print(i)


def count_arrangements(s, brokens):
    def count_helper(s, brokens):
        nonlocal count
        if s == '' and brokens == []:
            count += 1
            return
        if brokens and brokens[0] > len(s):
            return
        if s == '' and brokens != []:
            return
        if s != '' and brokens == []:
            return

        curr_count = brokens[0]

        if s[0] == '.':
            count_helper(s.lstrip('.'), brokens)  # skip all '.'
        if s[0] == '#':  # check if count of '#' matches the specs
            if all(c == '#' for c in (s[:curr_count])):
                if curr_count == len(s):
                    count += 1
                    return
                elif s[curr_count] == '?':
                    count += 1
                    count_helper(s[curr_count+1:].rstrip('.'), brokens[1:])
                elif s[curr_count] == '.':
                    count_helper(s[curr_count:].rstrip('.'), brokens[1:])
            else:
                return
        if s[0] == '?':
            count_helper('#' + s[1:], brokens)
            count_helper('.' + s[1:], brokens)

    count = 0
    count_helper(s, brokens)
    return count


assert count_arrangements('???.###', [1, 1, 3]) == 1

assert count_arrangements('?', [1]) == 1
assert count_arrangements('?.', [1]) == 1
assert count_arrangements('.?', [1]) == 1
assert count_arrangements('.?.', [1]) == 1
assert count_arrangements('..?.', [1]) == 1
assert count_arrangements('.?..', [1]) == 1
assert count_arrangements('..?..', [1]) == 1
assert count_arrangements('?..', [1]) == 1

assert count_arrangements('.??..??...?##.', [1, 1, 3]) == 4

# assert count_arrangements('?#?#?#?#?#?#?#?', [1, 3, 1, 6]) == 1
print(count_arrangements('?#?#?#?#?#?#?#?', [1, 3, 1, 6]))

# print(x)
