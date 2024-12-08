"""Advent of Code 2024 - Day 04"""

import os


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    lines = input_data.split("\n")
    word = "XMAS"
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    def is_valid(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])

    def search_from(x, y, dx, dy):
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or lines[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count


def mas(lines: list[str], i: int, j: int, reverse=False) -> bool:
    factor = 1 if not reverse else -1
    if lines[i + 1][j + 1 * factor] == "A":
        if lines[i][j] == "M" and lines[i + 2][j + 2 * factor] == "S":
            return True
        elif lines[i][j] == "S" and lines[i + 2][j + 2 * factor] == "M":
            return True

    return False


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    lines = input_data.split("\n")
    line_len = len(lines[0])
    count = 0

    for i in range(len(lines) - 2):
        for j in range(line_len - 2):
            if mas(lines, i, j) and mas(lines, i, j + 2, reverse=True):
                count += 1

    return count


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 18
    PART2_EXAMPLE_SOLUTION = 9

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
