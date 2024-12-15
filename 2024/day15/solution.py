"""Advent of Code 2024 - Day 15"""

import os


def parse_input(input_data: str):
    lines = input_data.split("\n\n")
    warehouse_map = lines[0].split("\n")
    moves = lines[1].replace("\n", "")
    return warehouse_map, moves


def read_map(warehouse_map: list[str]):
    pos = None
    boxes = set()
    for r, row in enumerate(warehouse_map):
        for c, char in enumerate(row):
            if char == "@":
                pos = (r, c)
            elif char == "O" or char == "[":
                boxes.add((r, c))

    return pos, boxes


def addt(x, y):
    return (x[0] + y[0], x[1] + y[1])


def left(pos):
    return (pos[0], pos[1] - 1)


def right(pos):
    return (pos[0], pos[1] + 1)


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    warehouse_map, moves = parse_input(input_data)
    pos, boxes = read_map(warehouse_map)
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    walls = set()
    for r, row in enumerate(warehouse_map):
        for c, char in enumerate(row):
            if char == "#":
                walls.add((r, c))

    def push(box, d):
        next_pos = addt(box, d)
        if next_pos in walls:
            return None
        if next_pos in boxes:
            r = push(next_pos, d)
            if r is None:
                return None
        boxes.remove(box)
        boxes.add(next_pos)
        return True

    for move in moves:
        dr, dc = directions[move]
        new_pos = addt(pos, (dr, dc))

        if new_pos in walls:
            continue

        if new_pos in boxes:
            copy = {x for x in boxes}
            r = push(new_pos, (dr, dc))
            if r is None:
                boxes = copy
                continue
        pos = new_pos

    return sum(100 * r + c for r, c in boxes)


def scale_map(warehouse_map: list[str]):
    scaled_map = []
    for row in warehouse_map:
        scaled_row = ""
        for char in row:
            if char == "#":
                scaled_row += "##"
            elif char == "O":
                scaled_row += "[]"
            elif char == ".":
                scaled_row += ".."
            elif char == "@":
                scaled_row += "@."
        scaled_map.append(scaled_row)
    return scaled_map


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    warehouse_map, moves = parse_input(input_data)
    scaled_map = scale_map(warehouse_map)
    pos, boxes = read_map(scaled_map)
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    walls = set()
    for r, row in enumerate(scaled_map):
        for c, char in enumerate(row):
            if char == "#":
                walls.add((r, c))

    def push(box, d):
        next_pos = addt(box, d)
        if next_pos in walls or right(next_pos) in walls:
            return None
        if d[0]:
            if next_pos in boxes:
                r = push(next_pos, d)
                if r is None:
                    return None
            if left(next_pos) in boxes:
                r = push(left(next_pos), d)
                if r is None:
                    return None
            if right(next_pos) in boxes:
                r = push(right(next_pos), d)
                if r is None:
                    return None
        if d[1] == 1:
            if right(next_pos) in boxes:
                r = push(right(next_pos), d)
                if r is None:
                    return None
        if d[1] == -1:
            if left(next_pos) in boxes:
                r = push(left(next_pos), d)
                if r is None:
                    return None
        boxes.remove(box)
        boxes.add(next_pos)
        return True

    for move in moves:
        dr, dc = directions[move]
        new_pos = addt(pos, (dr, dc))

        if new_pos in walls:
            continue

        if new_pos in boxes:
            copy = {x for x in boxes}
            r = push(new_pos, (dr, dc))
            if r is None:
                boxes = copy
                continue
        elif left(new_pos) in boxes:
            copy = {x for x in boxes}
            r = push(left(new_pos), (dr, dc))
            if r is None:
                boxes = copy
                continue
        pos = new_pos

    return sum(100 * r + c for r, c in boxes)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 10092
    PART2_EXAMPLE_SOLUTION = 9021

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
