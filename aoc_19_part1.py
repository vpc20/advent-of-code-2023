from collections import defaultdict

from aoc_tools import read_input_to_sections


def convert_to_dict(text):
    result = {}
    wf_code, wf_dtl = line.split('{')
    wf_dtls = wf_dtl[:-1]  # discard '}'

    wf_rules = []
    for wf_dtl in wf_dtls.split(','):
        if ':' in wf_dtl:
            k, v = wf_dtl.split(':')
            wf_rules.append({k:v})
        else:
            wf_rules.append({wf_dtl:None})

    result[wf_code] = wf_rules
    return result


def convert_to_list(text):
    result = []
    for rating in text.strip().lstrip('{').rstrip('}').split(','):
        k, v = rating.split('=')
        result.append({k:v})
    return result


if __name__ == '__main__':
    sections = read_input_to_sections('aoc_19_test_data1.txt')
    # print(len(sections))
    # print(sections[0])
    # print(sections[1])

    # workflows = [line for line in sections[0].strip().split()]
    # wf_dict = {e.split('{')[0]: e.split('{')[1][:-1] for e in workflows}
    # print(wf_dict)

    for line in sections[0].strip().split():
        wf_dict = convert_to_dict(line)
        print('wf_dict', wf_dict)

    for line in sections[1].strip().split():
        ratings_list = convert_to_list(line)
        print('ratings_list', ratings_list)


