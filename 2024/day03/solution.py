"""Advent of Code 2024 - Day 03"""

import os
import re


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", input_data)])


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    filtered_data = "".join(do.split("don't()")[0] for do in input_data.split("do()"))
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", filtered_data))


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 161
    PART2_EXAMPLE_SOLUTION = 48

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
