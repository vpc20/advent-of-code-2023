def count_arrangements(s, brokens):
    def count_helper(s, brokens):
        nonlocal count
        if s == '' and brokens == []:
            count += 1
            return
        if s == '' or brokens == []:
            return
        if brokens[0] > len(s):
            return

        curr_count = brokens[0]

        if s[0] == '.':
            count_helper(s.strip('.'), brokens)  # skip all '.'
        elif s[0] == '#':  # check if count of '#' matches the specs
            brokens[0] -= 1
            if brokens[0] == 0:
                if len(s) == 1:
                    count_helper(s[1:].strip('.'), brokens[1:])
                elif s[1] == '.':
                    count_helper(s[1:].strip('.'), brokens[1:])
                elif s[1] == '?':
                    count_helper(s[2:].strip('.'), brokens[1:])
                    count_helper(s[2:].replace('?', '#', 1).strip('.'), brokens[1:])
            else:
                count_helper(s[1:].strip('.'), brokens)
        elif s[0] == '?':
            count_helper(s.replace('?', '#', 1), brokens)
            count_helper(s.replace('?', '.', 1), brokens)

    count = 0
    count_helper(s, brokens)
    return count


x = count_arrangements('???.###', [1, 1, 3])
print(x)

assert count_arrangements('?', [1]) == 1
assert count_arrangements('?.', [1]) == 1
assert count_arrangements('.?', [1]) == 1
assert count_arrangements('.?.', [1]) == 1
assert count_arrangements('..?.', [1]) == 1
assert count_arrangements('.?..', [1]) == 1
assert count_arrangements('..?..', [1]) == 1
assert count_arrangements('?..', [1]) == 1

# assert count_arrangements('???.###', [1, 1, 3]) == 1
assert count_arrangements('.??..??...?##.', [1, 1, 3]) == 4

# assert count_arrangements('?#?#?#?#?#?#?#?', [1, 3, 1, 6]) == 1
# print(count_arrangements('?#?#?#?#?#?#?#?', [1, 3, 1, 6]))
