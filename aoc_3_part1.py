from aoc_tools import read_input_to_grid


# part 1
# f = open('aoc_3_test_data1.txt')
# f = open('aoc_3_data1.txt')

def is_adjacent_to_symbol(grid, row, col):
    nrows = len(grid)
    ncols = len(grid[0])
    for nr, nc in ([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),  # adjacent rows and columns
                    (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]):
        if 0 <= nr < nrows and 0 <= nc < ncols:
            if not grid[nr][nc].isdigit() and grid[nr][nc] != '.':  # symbol is not digit and not '.'
                return True
    return False


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


def part_numbers_sum(grid, num_coords):
    sum_part_numbers = 0
    for start_coord, end_coord, part_number in num_coords:
        print(start_coord, end_coord, part_number)
        start_row, start_col = start_coord
        end_row, end_col = end_coord
        for col in range(start_col, end_col):
            if is_adjacent_to_symbol(grid, start_row, col):
                sum_part_numbers += part_number
                break
    return sum_part_numbers


def solve_part1():
    # grid = read_input_to_grid('aoc_3_test_data1.txt')
    grid = read_input_to_grid('aoc_3_data1.txt')
    num_coords = find_numbers_in_grid(grid)
    return part_numbers_sum(grid, num_coords)


if __name__ == '__main__':
    print(solve_part1())
    # 527364
