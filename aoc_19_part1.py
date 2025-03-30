from collections import defaultdict

from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    sections = read_input_to_sections('aoc_19_test_data1.txt')
    # print(len(sections))
    # print(sections[0])
    # print(sections[1])

    # d1 = defaultdict()
    # for line in sections[0].strip().split():
    #     print(line)
    #     l1 = line.split('{')
    #     print(l1)
    #     d1[l1[0]] = l1[1][:-1]
    # print('----------------')
    # print(d1)

    workflows = [line for line in sections[0].strip().split()]
    wf_dict = {e.split('{')[0]: e.split('{')[1][:-1] for e in workflows}
    print(wf_dict)

    # d1 = {x[0]: x[1][:-1] for x in line.split('{')}
    # print(d1)

    # px:['a<2006':'qkq', 'm > 2090': 'A', rfg]