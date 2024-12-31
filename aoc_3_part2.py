from collections import defaultdict

from aoc_tools import read_input_to_grid


def find_numbers_in_grid(grid):
    num_coords = []
    for i, row in enumerate(grid):
        digit_found = False
        number_in_grid = ''
        for j, char in enumerate(row):
            if char.isdigit():
                if digit_found is False:
                    start_coord = (i, j)
                    digit_found = True
                number_in_grid += grid[i][j]
            else:
                if digit_found is True:
                    end_coord = (i, j)
                    num_coords.append((start_coord, end_coord, int(number_in_grid)))
                    digit_found = False
                    number_in_grid = ''
        if digit_found is True:
            end_coord = (i, len(row))
            num_coords.append((start_coord, end_coord, int(number_in_grid)))
    return num_coords


def is_adjacent_to_gear(grid, row, col):
    nrows = len(grid)
    ncols = len(grid[0])
    is_gear = False
    gear_coords = []

    for nr, nc in ([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),  # adjacent rows and columns
                    (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]):
        if 0 <= nr < nrows and 0 <= nc < ncols:
            # if not grid[nr][nc].isdigit() and grid[nr][nc] != '.':  # symbol is not digit and not '.'
            #     is_symbol = True
            if grid[nr][nc] == '*':
                is_gear = True
                gear_coords.append((nr, nc))
    return is_gear, gear_coords


def find_gears(grid, num_coords):
    sum_gear_ratios = 0
    gear_dict = defaultdict(set)
    for start_coord, end_coord, part_number in num_coords:
        # print(start_coord, end_coord, part_number)
        start_row, start_col = start_coord
        end_row, end_col = end_coord
        for col in range(start_col, end_col):
            is_gear, gear_coords = is_adjacent_to_gear(grid, start_row, col)
            if is_gear:
                for gear_coord in gear_coords:
                    gear_dict[gear_coord].add((start_coord, end_coord, part_number))
    for k, v in gear_dict.items():
        print(k, v)
    print()
    for k, v in gear_dict.items():
        if len(v) == 2:  # a gear is any * symbol that is adjacent to exactly two part numbers
            print(k, v)
            num1_info, num2_info = v
            _, _, n1 = num1_info
            _, _, n2 = num2_info
            sum_gear_ratios += n1 * n2
    return sum_gear_ratios


def solve_part2():
    # grid = read_input_to_grid('aoc_3_test_data1.txt')
    grid = read_input_to_grid('aoc_3_data1.txt')
    num_coords = find_numbers_in_grid(grid)
    return find_gears(grid, num_coords)


if __name__ == '__main__':
    print(solve_part2())
    # 79026871
