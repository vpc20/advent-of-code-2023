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
    total = 0

    for nums in all_nums:
        all_seqs = gen_all_seq(nums)
        sum_last_element = 0
        for i in range(len(all_seqs) - 2, -1, -1):
            sum_last_element +=  all_seqs[i][-1]
        total += sum_last_element

    print(total)

# 1647269739
