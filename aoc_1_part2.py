import re

# part 2
d = {'one': '1', '1': '1',
     'two': '2', '2': '2',
     'three': '3', '3': '3',
     'four': '4', '4': '4',
     'five': '5', '5': '5',
     'six': '6', '6': '6',
     'seven': '7', '7': '7',
     'eight': '8', '8': '8',
     'nine': '9', '9': '9'}

# f = open('aoc_1_test_data2.txt')
# f = open('aoc_1_test_data3.txt')
f = open('aoc_1_data1.txt')

# string_lst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# sjoin = '|'.join(string_lst)
# print(sjoin)

all_nums = [re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line) for line in f]
print(all_nums)
total_calibration = sum(int(d[nums[0]] + d[nums[-1]]) for nums in all_nums)
print(total_calibration)

# for nums in all_nums:
#      print(nums[0], d[nums[0]], nums[-1], d[nums[-1]])
#      print(int(d[nums[0]] + d[nums[-1]]))

f.close()

# 54978 incorrect
