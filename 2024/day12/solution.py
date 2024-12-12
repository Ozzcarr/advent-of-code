"""Advent of Code 2024 - Day 12"""

import os


def floodfill(grid: list[str], r: int, c: int, color: str, checked_coordinates: set) -> tuple[int, int, int]:
    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
        return 0, 1, checked_coordinates
    if grid[r][c] != color or (r, c) in checked_coordinates:
        return 0, 1 if grid[r][c] != color else 0, checked_coordinates

    checked_coordinates.add((r, c))
    total_area = 1
    total_perimeter = 0

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        area, perimeter, region = floodfill(grid, r + dr, c + dc, color, checked_coordinates)
        total_area += area
        total_perimeter += perimeter

    return total_area, total_perimeter, checked_coordinates


def sides(region: set, width: int, height: int) -> int:
    return 0


def price(grid: list[str], part2=False) -> int:
    checked_coordinates = set()
    total_price = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in checked_coordinates:
                area, perimeter, region = floodfill(grid, r, c, grid[r][c], set())
                checked_coordinates = checked_coordinates.union(region)
                total_price += area * (sides(region, len(grid), len(grid[0])) if part2 else perimeter)

    return total_price


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return price(input_data.split("\n"))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    return price(input_data.split("\n"), True)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 1930
    PART2_EXAMPLE_SOLUTION = 1206

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
