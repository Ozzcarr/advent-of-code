"""Advent of Code 2024 - Day 02"""

import os


def is_safe(row):
    return all(0 < (x - y) <= 3 for x, y in zip(row[1:], row)) or all(-3 <= (x - y) < 0 for x, y in zip(row[1:], row))


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    data = list(map(lambda x: list(map(int, x.split())), input_data.split("\n")))
    return sum(is_safe(row) for row in data)


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    data = list(map(lambda x: list(map(int, x.split())), input_data.split("\n")))
    return sum(any([is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))]) for row in data)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 2
    PART2_EXAMPLE_SOLUTION = 4

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
