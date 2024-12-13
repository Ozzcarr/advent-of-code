"""Advent of Code 2024 - Day 13"""

import os

import numpy as np


def solve(input_data: str, p: int = 0) -> int:
    M = np.fromregex(input_data, r"\d+", [("", int)] * 6).view(int).reshape(-1, 3, 2).swapaxes(1, 2)
    S = M[..., :2]
    P = M[..., 2:] + p
    R = np.linalg.solve(S, P).round().astype(int)
    return (R.squeeze() @ [3, 1] @ (S @ R == P).all(1)).sum()


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return solve(input_data)


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    return solve(input_data, 1e13)


def get_filepath(filename: str):
    """Gets the file path."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    return file_path


def main():
    example_input = get_filepath("example.txt")
    puzzle_input = get_filepath("input.txt")

    PART1_EXAMPLE_SOLUTION = 480

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    print("Part 2:", part2(puzzle_input))


if __name__ == "__main__":
    main()
