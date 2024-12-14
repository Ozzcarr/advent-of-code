"""Advent of Code 2024 - Day 14"""

import os


def parse_input(input_data):
    robots = []
    for line in input_data.split("\n"):
        p, v = line.split()
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append(((px, py), (vx, vy)))
    return robots


def simulate_robots(robots, width, height, seconds):
    for _ in range(seconds):
        new_positions = []
        for (px, py), (vx, vy) in robots:
            new_px = (px + vx) % width
            new_py = (py + vy) % height
            new_positions.append((new_px, new_py))
        robots = [(pos, vel) for pos, (_, vel) in zip(new_positions, robots)]
    return [pos for pos, _ in robots]


def simulate_easter_egg(robots, width, height):
    seconds = 0
    while True:
        new_positions = []
        positions_set = set()
        all_unique = True

        for (px, py), (vx, vy) in robots:
            new_px = (px + vx) % width
            new_py = (py + vy) % height
            new_positions.append((new_px, new_py))
            if (new_px, new_py) in positions_set:
                all_unique = False
            positions_set.add((new_px, new_py))

        robots = [(pos, vel) for pos, (_, vel) in zip(new_positions, robots)]
        seconds += 1

        if all_unique:
            break

    return seconds


def count_robots_in_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in robots:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1

    return quadrants


def calculate_safety_factor(quadrants):
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    width, height = 101, 103
    robots = parse_input(input_data)
    final_positions = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(final_positions, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    return safety_factor


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    width, height = 101, 103
    robots = parse_input(input_data)
    seconds = simulate_easter_egg(robots, width, height)
    return seconds


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 21

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    print("Part 2:", part2(puzzle_input))


if __name__ == "__main__":
    main()
