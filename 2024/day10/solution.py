"""Advent of Code 2024 - Day 10"""

import os


def parse_input(input_data: str):
    return [list(map(int, line)) for line in input_data.splitlines()]


def dfs(parsed_map, x, y, visited=None, current_height=0):
    if parsed_map[x][y] != current_height:
        return 0

    if current_height == 9:
        if visited is not None:
            if (x, y) not in visited:
                visited.add((x, y))
                return 1
            else:
                return 0
        else:
            return 1

    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < len(parsed_map) and 0 <= y + dy < len(parsed_map[0]):
            count += dfs(parsed_map, x + dx, y + dy, visited, current_height + 1)

    return count


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    parsed_map = parse_input(input_data)
    return sum(dfs(parsed_map, i, j, set()) for i in range(len(parsed_map)) for j in range(len(parsed_map[0])))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    parsed_map = parse_input(input_data)
    return sum(dfs(parsed_map, i, j) for i in range(len(parsed_map)) for j in range(len(parsed_map[0])))


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 36
    PART2_EXAMPLE_SOLUTION = 81

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
