"""Advent of Code 2024 - Day 08"""

import os
from itertools import permutations


def parse_input(lines: list[str]):
    antennas = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char.isalnum():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    grid = input_data.split("\n")
    antennas = parse_input(grid)
    positions = set()

    for frequency in antennas.keys():
        for (r1, c1), (r2, c2) in permutations(antennas[frequency], 2):
            dr = r2 - r1
            dc = c2 - c1
            if 0 <= r1 + 2 * dr < len(grid) and 0 <= c1 + 2 * dc < len(grid[0]):
                positions.add((r1 + 2 * dr, c1 + 2 * dc))

    return len(positions)


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    grid = input_data.split("\n")
    antennas = parse_input(grid)
    positions = set()

    for frequency in antennas.keys():
        for (r1, c1), (r2, c2) in permutations(antennas[frequency], 2):
            dr = r2 - r1
            dc = c2 - c1
            n = 1
            while 0 <= r1 + n * dr < len(grid) and 0 <= c1 + n * dc < len(grid[0]):
                positions.add((r1 + n * dr, c1 + n * dc))
                n += 1

    return len(positions)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 14
    PART2_EXAMPLE_SOLUTION = 34

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
