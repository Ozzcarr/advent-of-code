"""Advent of Code 2024 - Day 07"""

import os


def parse_line(line: str):
    test_value, numbers = line.split(": ")
    return int(test_value), list(map(int, numbers.split()))


def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "|":
            result = int(str(result) + str(numbers[i + 1]))

    return result


def algorithm(line: str, operations: str) -> int:
    test_value, numbers = parse_line(line)
    from itertools import product
    for operators in product(operations, repeat=len(numbers) - 1):
        if evaluate(numbers, operators) == test_value:
            return test_value

    return 0


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return sum(algorithm(line, operations="+*") for line in input_data.split("\n"))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    return sum(algorithm(line, operations="+*|") for line in input_data.split("\n"))


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 3749
    PART2_EXAMPLE_SOLUTION = 11387

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
