"""Advent of Code 2023 - Day 01"""

import os
import re


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return sum(int(re.findall(r"(\d)", line)[0] + re.findall(r"(\d)", line)[-1]) for line in input_data.split("\n"))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    first_digit = None
    last_digit = None
    total = 0

    for line in input_data.split("\n"):
        left = float("inf")
        right = float("-inf")
        left_number = None
        right_number = None

        for number in number_dict:
            if number in line:
                if line.find(number) < left:
                    left = line.find(number)
                    left_number = number

                if line.rfind(number) > right:
                    right = line.rfind(number)
                    right_number = number

        if left_number:
            line = line.replace(left_number, number_dict[left_number], 1)

        if right_number:
            line = line.replace(right_number, number_dict[right_number])

        for char in line:
            if char.isdigit():
                first_digit = char
                break

        for char in line[::-1]:
            if char.isdigit():
                last_digit = char
                break

        number = int(first_digit + last_digit)
        total += number

    return total


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    example2_input = read_file("example2.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 142
    PART2_EXAMPLE_SOLUTION = 281

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    part2_example_solution = part2(example2_input)
    if part2_example_solution == PART2_EXAMPLE_SOLUTION:
        print("Part 2:", part2(puzzle_input))
    else:
        print(f"Part 2 Failed: {part2_example_solution} != {PART2_EXAMPLE_SOLUTION}")


if __name__ == "__main__":
    main()
