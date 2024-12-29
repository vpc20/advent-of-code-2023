import re

# part 1
# f = open('aoc_1_test_data1.txt')
f = open('aoc_1_data1.txt')
all_nums = [re.findall(r'\d', line) for line in f]
print(all_nums)
total_calibration = sum([int(nums[0] + nums[-1]) for nums in all_nums])
print(total_calibration)
f.close()

