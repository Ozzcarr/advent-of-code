"""Advent of Code 2024 - Day 01"""

import os
import re
from collections import Counter


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    l, r = map(sorted, zip(*re.findall(r"(\d+)\s+(\d+)", input_data)))
    return sum([abs(int(x) - int(y)) for x, y in zip(l, r)])


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    l, r = zip(*re.findall(r"(\d+)\s+(\d+)", input_data))
    return sum([int(v) * int(Counter(r).get(v, 0)) for v in l])


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 11
    PART2_EXAMPLE_SOLUTION = 31

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
