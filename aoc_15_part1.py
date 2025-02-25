

def hash_val(s):
    curr_val = 0
    for c in s:
        curr_val += ord(c)
        curr_val *= 17
        curr_val %= 256
    print(curr_val)
    return curr_val


if __name__ == '__main__':
    # f = open('aoc_15_test_data1.txt')
    f = open('aoc_15_data1.txt')
    input = f.read().split(',')
    f.close()

    total_hash = 0
    for e in input:
        hv = hash_val(e.strip())
        total_hash += hv

    print(total_hash)

    # print(hash_val('HASH'))