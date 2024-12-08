"""Advent of Code 2024 - Day 06"""

import os


def parse_input(input_str: str):
    map_lines = [list(line) for line in input_str.strip().split("\n")]
    guard_pos = None
    guard_dir = None
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            if char in directions:
                guard_pos = (x, y)
                guard_dir = directions[char]
                break
        if guard_pos:
            break

    return map_lines, guard_pos, guard_dir


def turn_right(direction):
    turns = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    return turns[direction]


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    map_lines, guard_pos, guard_dir = parse_input(input_data)
    visited_positions = set()
    width = len(map_lines[0])
    height = len(map_lines)

    while True:
        visited_positions.add(guard_pos)
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])

        if 0 <= next_pos[1] < width and 0 <= next_pos[0] < height:
            if map_lines[next_pos[1]][next_pos[0]] != "#":
                guard_pos = next_pos
            else:
                guard_dir = turn_right(guard_dir)
        else:
            break

    return len(visited_positions)


def part2_algorithm(map_lines, guard_pos, guard_dir, obstruction=None) -> tuple[bool, set]:
    seen_states = set()
    width = len(map_lines[0])
    height = len(map_lines)
    grid = [row[:] for row in map_lines]

    if obstruction:
        row, column = obstruction
        grid[row][column] = "#"

    while (guard_pos, guard_dir) not in seen_states:
        seen_states.add((guard_pos, guard_dir))
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])

        if 0 <= next_pos[1] < width and 0 <= next_pos[0] < height:
            if grid[next_pos[1]][next_pos[0]] != "#":
                guard_pos = next_pos
            else:
                guard_dir = turn_right(guard_dir)
        else:
            return False, set(state[0] for state in seen_states)

    return True, set(state[0] for state in seen_states)


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    map_lines, guard_pos, guard_dir = parse_input(input_data)
    _, positions = part2_algorithm(map_lines, guard_pos, guard_dir)

    total = 0
    for y, x in positions:
        if map_lines[x][y] != "#" and (x, y) != guard_pos:
            total += part2_algorithm(map_lines, guard_pos, guard_dir, (x, y))[0]

    return total


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 41
    PART2_EXAMPLE_SOLUTION = 6

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
