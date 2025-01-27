import re

from aoc_tools import read_input_to_sections


def navigate_desert(lr_instructions, nodes_dict, curr_nodes):
    steps = 0
    end_of_navigation = False
    while not end_of_navigation:
        for direction in lr_instructions:
            end_nodes = []
            for node in curr_nodes:
                if direction == 'L':
                    end_nodes.append(nodes_dict[node][0])
                else:
                    end_nodes.append(nodes_dict[node][1])
            steps += 1
            # print(steps, end_nodes)
            curr_nodes = end_nodes[:]
            if all(nodes.endswith('Z') for nodes in end_nodes):
                end_of_navigation = True
                break
        # print('directions exhausted')
    return steps


if __name__ == '__main__':

    sections = read_input_to_sections('aoc_8_test_data3.txt')
    lr_instructions = sections[0]
    print(lr_instructions)

    all_nodes = [re.findall(r'[A-Z0-9]{3}', line) for line in sections[1].split('\n')]
    nodes_dict = {nodes[0]: (nodes[1], nodes[2]) for nodes in all_nodes}
    for k, v in nodes_dict.items():
        print(k, v)

    start_nodes = [k for k in nodes_dict.keys() if k.endswith('A')]
    print(start_nodes)

    print(navigate_desert(lr_instructions, nodes_dict, start_nodes))

    # for k in nodes_dict.keys():
    #     if k.endswith('Z'):
    #         print(k)
