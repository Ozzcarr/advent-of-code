"""Advent of Code 2023 - Day 04"""

import os
import re
from collections import Counter


def parse_lines(lines: str):
    rows = lines.split("\n")
    nums = [[list(map(int, re.findall(r"(\d+)", card))) for card in row.split(":")[1].split("|")] for row in rows]
    return [sum(Counter(y).get(v, 0) for v in x) for x, y in nums]


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return sum(int(2 ** (v - 1)) for v in parse_lines(input_data))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    cards = parse_lines(input_data)
    num_cards = len(cards)
    counts = [1] * num_cards

    for i in range(num_cards):
        for j in range(i + 1, min(i + 1 + cards[i], num_cards)):
            counts[j] += counts[i]

    return sum(counts)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 13
    PART2_EXAMPLE_SOLUTION = 30

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
