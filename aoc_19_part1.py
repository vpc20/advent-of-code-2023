# from collections import defaultdict
from collections import OrderedDict

from aoc_tools import read_input_to_sections


def convert_rules_to_dict(text):
    result = OrderedDict()
    for wf_dtl in wf_dtls.split(','):
        if ':' in wf_dtl:
            k, v = wf_dtl.split(':')
            result[k] = v
        else:
            result[wf_dtl] = None
    return result


def convert_ratings_to_dict(text):
    result = OrderedDict()
    for rating in text.strip().lstrip('{').rstrip('}').split(','):
        k, v = rating.split('=')
        result[k] = v
    return result


def apply_workflow(ratings_dict, wf_dict):
    for part_code, part_val in ratings_dict.items():
        print(part_code, part_val)
        rules_dict = wf_dict['in']
        pass


if __name__ == '__main__':
    sections = read_input_to_sections('aoc_19_test_data1.txt')
    # print(len(sections))
    # print(sections[0])
    # print(sections[1])

    # workflows = [line for line in sections[0].strip().split()]
    # wf_dict = {e.split('{')[0]: e.split('{')[1][:-1] for e in workflows}
    # print(wf_dict)

    wf_dict = {}
    for line in sections[0].strip().split():
        wf_code, wf_dtls = line.strip().split('{')
        wf_dtls = wf_dtls.rstrip('}')
        rules_dict = convert_rules_to_dict(wf_dtls)
        wf_dict[wf_code] = rules_dict

    print('wf_dict')
    for k, v in wf_dict.items():
        print(k, v)

    ratings_list = []
    for line in sections[1].strip().split():
        ratings_dict = convert_ratings_to_dict(line)
        ratings_list.append(ratings_dict)
    print('ratings_list')
    for e in ratings_list:
        print(e)

    print()
    for ratings_dict in ratings_list:
        print(ratings_dict, type(ratings_dict))
        apply_workflow(ratings_dict, wf_dict)
