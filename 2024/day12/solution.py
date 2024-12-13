"""Advent of Code 2024 - Day 12"""

import os
from collections import defaultdict


def floodfill(grid: list[str], r: int, c: int, color: str, checked_coordinates: set) -> tuple[int, int]:
    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
        return 0, 1
    if grid[r][c] != color or (r, c) in checked_coordinates:
        return 0, 1 if grid[r][c] != color else 0

    checked_coordinates.add((r, c))
    total_area = 1
    total_perimeter = 0

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        area, perimeter = floodfill(grid, r + dr, c + dc, color, checked_coordinates)
        total_area += area
        total_perimeter += perimeter

    return total_area, total_perimeter


def floodfill2(grid: list[str], r: int, c: int, color: str, visited: list[str], sides) -> int:
    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or visited[r][c] is not None or grid[r][c] != color:
        return 0
    visited[r][c] = color
    total_area = 1

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]) or grid[nr][nc] != color:
            if c != nc:
                sides[('v', c, c > nc)].append(r)
            else:
                sides[('h', r, r > nr)].append(c)
        else:
            total_area += floodfill2(grid, nr, nc, color, visited, sides)

    return total_area


def calculate_sides(sides) -> int:
    total_sides = 0
    for _, side_row in sides.items():
        side_row.sort()
        for i in range(1, len(side_row)):
            if (side_row[i - 1] + 1) != side_row[i]:
                total_sides += 1
        total_sides += 1
    return total_sides


def price(grid: list[str], part2=False) -> int:
    checked_coordinates = set()
    total_price = 0
    visited = [[None] * len(grid[0]) for _ in range(len(grid))]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in checked_coordinates:
                if part2:
                    sides = defaultdict(list)
                    area = floodfill2(grid, r, c, grid[r][c], visited, sides)
                    sides = calculate_sides(sides)
                    total_price += area * sides
                else:
                    area, perimeter = floodfill(grid, r, c, grid[r][c], checked_coordinates)
                    total_price += area * perimeter

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
