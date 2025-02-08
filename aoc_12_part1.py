import itertools


def validate_arrangement(s, damage):
    # print(s, damage)
    hash_list = [e for e in (s.split('.')) if e != '']
    # print(hash_list)
    hash_counts = [e.count('#') for e in hash_list]
    # print(hash_counts)
    return hash_counts == damage


if __name__ == '__main__':
    f = open('aoc_12_data1.txt')
    input = [line.strip().split() for line in f]
    f.close()

    patterns = [item[0] for item in input]
    damages = [[int(e) for e in item[1].strip().split(',')] for item in input]

    sum_count = 0
    for i, pattern in enumerate(patterns):
        print(pattern)
        arr = ['.#' for i in range(pattern.count('?'))]
        # print('pattern', pattern)
        for p in itertools.product(*arr):
            # print(p)
            iterp = iter(p)
            s = ''.join(next(iterp) if c == '?' else c for c in pattern)
            # print(s)
            if validate_arrangement(s, damages[i]):
                sum_count += 1


    print(sum_count)
