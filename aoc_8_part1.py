import re

from aoc_tools import read_input_to_sections


def navigate_desert(lr_instructions, nodes_dict):
    steps = 0
    curr_node = 'AAA'
    last_node = 'ZZZ'
    while curr_node != last_node:
        for direction in lr_instructions:
            if direction == 'L':
                curr_node = nodes_dict[curr_node][0]
            else:
                curr_node = nodes_dict[curr_node][1]
            steps += 1
    return steps


if __name__ == '__main__':
    # f = open('aoc_8_data1.txt')
    # for line in f:
    #     lr_instructions = line.strip()
    # f.close()
    #
    # f = open('aoc_8_data1b.txt')
    # all_nodes = [re.findall(r'[A-Z]{3}', line) for line in f]
    # nodes_dict = {nodes[0]: (nodes[1], nodes[2]) for nodes in all_nodes}
    # f.close()
    # for k, v in nodes_dict.items():
    #     print(k, v)

    sections = read_input_to_sections('aoc_8_data1.txt')
    lr_instructions = sections[0]
    print(lr_instructions)

    all_nodes = [re.findall(r'[A-Z]{3}', line) for line in sections[1].strip().split('\n')]
    for nodes in all_nodes:
        print(nodes)
    nodes_dict = {nodes[0]: (nodes[1], nodes[2]) for nodes in all_nodes}
    # for k, v in nodes_dict.items():
    #     print(k, v)

    print(navigate_desert(lr_instructions, nodes_dict))

    # for k in nodes_dict.keys():
    #     if k.endswith('A'):
    #         print(k)
    #
    # for k in nodes_dict.keys():
    #     if k.endswith('Z'):
    #         print(k)
