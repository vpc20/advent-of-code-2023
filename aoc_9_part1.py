from aoc_tools import read_input_to_nums


def gen_all_seq(nums):
    all_seqs = [nums]
    while not all((num == 0 for num in nums)):
        nxt = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        all_seqs.append(nxt)
        nums = nxt[:]
    return all_seqs


if __name__ == '__main__':
    # all_nums = read_input_to_nums('aoc_9_test_data1.txt')
    # all_nums = read_input_to_nums('aoc_9_test_data2.txt')
    all_nums = read_input_to_nums('aoc_9_data1.txt')
    total1, total2 = 0, 0

    for nums in all_nums:
        all_seqs = gen_all_seq(nums)

        sum_last_element = 0  # for part2 of problem
        for i in range(len(all_seqs) - 2, -1, -1):
            sum_last_element += all_seqs[i][-1]
        total1 += sum_last_element

        diff_first_element = 0  # for part2 of problem
        for e in all_seqs:
            print(e)
        for i in range(len(all_seqs) - 2, -1, -1):
            diff_first_element = all_seqs[i][0] - diff_first_element
        total2 += diff_first_element

    print(total1)
    print(total2)

# 1647269739
