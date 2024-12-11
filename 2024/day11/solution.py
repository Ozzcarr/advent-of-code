"""Advent of Code 2024 - Day 11"""

import os
from collections import defaultdict


def blink(stones: list[int], times: int = 25) -> int:
    counts = defaultdict(int)
    for stone in stones:
        counts[stone] += 1

    for _ in range(times):
        new_counts = defaultdict(int)
        for stone, count in counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                half_len = len(stone) // 2
                new_counts[int(stone[:half_len])] += count
                new_counts[int(stone[half_len:])] += count
            else:
                new_counts[stone * 2024] += count

        counts = new_counts

    return sum(counts.values())


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return blink(list(map(int, input_data.split())))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    return blink(list(map(int, input_data.split())), times=75)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 55312

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    print("Part 2:", part2(puzzle_input))


if __name__ == "__main__":
    main()
