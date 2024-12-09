"""Advent of Code 2023 - Day 02"""

import os


def parse_line(line: str) -> tuple[int, list[dict]]:
    game = int(line.split()[1].strip(":"))
    sets = line.split(":")[1].split(";")
    cubes_per_set = []
    for item_set in sets:
        set_data = item_set.split(",")
        color_occurrences = {}
        for color_data in set_data:
            number, color = color_data.strip().split()
            color_occurrences[color] = int(number)

        cubes_per_set.append(color_occurrences)

    return game, cubes_per_set


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    RED_CUBES = 12
    GREEN_CUBES = 13
    BLUE_CUBES = 14

    total = 0
    for line in input_data.split("\n"):
        game, cube_occurrences = parse_line(line)
        valid_game = True
        for set in cube_occurrences:
            for color in set:
                match color:
                    case "red":
                        if set[color] > RED_CUBES:
                            valid_game = False
                    case "green":
                        if set[color] > GREEN_CUBES:
                            valid_game = False
                    case "blue":
                        if set[color] > BLUE_CUBES:
                            valid_game = False

        if valid_game:
            total += game

    return total


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    total = 0
    for line in input_data.split("\n"):
        game, cube_occurrences = parse_line(line)
        min_red, min_green, min_blue = 0, 0, 0
        for set in cube_occurrences:
            for color in set:
                match color:
                    case "red":
                        min_red = max(min_red, set[color])
                    case "green":
                        min_green = max(min_green, set[color])
                    case "blue":
                        min_blue = max(min_blue, set[color])

        total += min_red * min_green * min_blue

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

    PART1_EXAMPLE_SOLUTION = 8
    PART2_EXAMPLE_SOLUTION = 2286

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
