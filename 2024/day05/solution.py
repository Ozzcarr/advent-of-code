"""Advent of Code 2024 - Day 05"""

import os
import re


def parse_input(input_str: str):
    rules = re.findall(r"(\d+)\|(\d+)", input_str)
    updates = [update.split(",") for update in input_str.split("\n\n")[1].split("\n")]
    return rules, updates


def is_update_correct(rules, update):
    for x, y in rules:
        if x in update and y in update:
            if int(update.index(x)) > int(update.index(y)):
                return False
    return True


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    rules, updates = parse_input(input_data)
    correct_updates = [update for update in updates if is_update_correct(rules, update)]
    return sum(int(update[len(update) // 2]) for update in correct_updates)


def sort_update(rules, update):
    position = {num: i for i, num in enumerate(update)}

    for _ in range(len(update)):
        for x, y in rules:
            if x in position and y in position:
                if position[x] > position[y]:
                    position[x], position[y] = position[y], position[x]
                    update[position[x]], update[position[y]] = update[position[y]], update[position[x]]

    return update


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    rules, updates = parse_input(input_data)
    incorrect_updates = [update for update in updates if not is_update_correct(rules, update)]
    sorted_updates = [sort_update(rules, update) for update in incorrect_updates]
    return sum(int(update[len(update) // 2]) for update in sorted_updates)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 143
    PART2_EXAMPLE_SOLUTION = 123

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
