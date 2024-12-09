"""Advent of Code 2023 - Day 03"""

import os


def is_symbol(char: str) -> bool:
    return char not in "1234567890."


def get_adjacent_indices(row: int, col: int):
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]


def extract_number(schematic, row, col, cols):
    while col > 0 and schematic[row][col - 1].isdigit():
        col -= 1

    number_str = ""
    while col < cols and schematic[row][col].isdigit():
        number_str += schematic[row][col]
        col += 1

    return int(number_str), col


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    schematic = [line for line in input_data.split("\n")]
    rows = len(schematic)
    cols = len(schematic[0])

    total = 0
    for row in range(rows):
        col = 0
        while col < cols:
            if schematic[row][col].isdigit():
                number, col = extract_number(schematic, row, col, cols)
                start_col = col - len(str(number))

                if any(
                    0 <= r < rows and 0 <= c < cols and is_symbol(schematic[r][c])
                    for digit_col in range(start_col, col)
                    for r, c, in get_adjacent_indices(row, digit_col)
                ):
                    total += number
            else:
                col += 1

    return total


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    schematic = input_data.split("\n")
    rows, cols = len(schematic), len(schematic[0])
    processed_positions = set()

    def get_part_numbers(row, col):
        part_numbers = []
        for r, c in get_adjacent_indices(row, col):
            if 0 <= r < rows and 0 <= c < cols and schematic[r][c].isdigit():
                if (r, c) not in processed_positions:
                    number, end_col = extract_number(schematic, r, c, cols)
                    part_numbers.append(number)
                    for number_col in range(c, end_col):
                        processed_positions.add((r, number_col))
        return part_numbers

    total = 0
    for row in range(rows):
        for col in range(cols):
            if schematic[row][col] == "*":
                part_numbers = get_part_numbers(row, col)
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total += gear_ratio

    return total


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 4361
    PART2_EXAMPLE_SOLUTION = 467835

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    part2_example_solution = part2(example_input)
    if part2_example_solution == PART2_EXAMPLE_SOLUTION:
        print("Part 2:", part2(puzzle_input))
    else:
        print(f"Part 2 Failed: {part2_example_solution} != {PART2_EXAMPLE_SOLUTION}")


if __name__ == "__main__":
    main()
