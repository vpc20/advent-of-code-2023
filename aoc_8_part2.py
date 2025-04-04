import re
from math import lcm

from aoc_tools import read_input_to_sections


def navigate_desert(lr_instructions, nodes_dict, curr_nodes):
    steps = 0
    steps_list = []
    for curr_node in curr_nodes:
        node = curr_node
        end_of_navigation = False
        while not end_of_navigation:
            for direction in lr_instructions:
                if direction == 'L':
                    end_node = nodes_dict[node][0]
                else:
                    end_node = nodes_dict[node][1]
                steps += 1
                node = end_node
                if end_node.endswith('Z'):
                    end_of_navigation = True
                    steps_list.append(steps)
                    break
    print(steps_list)
    return lcm(*steps_list)


if __name__ == '__main__':

    sections = read_input_to_sections('aoc_8_data1.txt')
    lr_instructions = sections[0]
    print(lr_instructions)

    all_nodes = [re.findall(r'[A-Z0-9]{3}', line) for line in sections[1].strip().split('\n')]
    nodes_dict = {nodes[0]: (nodes[1], nodes[2]) for nodes in all_nodes}
    for k, v in nodes_dict.items():
        print(k, v)

    start_nodes = [k for k in nodes_dict.keys() if k.endswith('A')]
    print(start_nodes)

    print(navigate_desert(lr_instructions, nodes_dict, start_nodes))

    # for k in nodes_dict.keys():
    #     if k.endswith('Z'):
    #         print(k)
