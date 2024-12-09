"""Advent of Code 2024 - Day 09"""

import os


def parse_disk(input_data: str):
    disk = []

    id = 0
    for i, num in enumerate(input_data):
        if i % 2 == 0:
            for _ in range(int(num)):
                disk.append(id)
            id += 1
        else:
            for _ in range(int(num)):
                disk.append(".")

    return disk


def compact_disk(disk: list) -> list[int]:
    j = len(disk) - 1
    for i in range(j + 1):
        if disk[i] != ".":
            continue

        while disk[j] == "." and j > i:
            j -= 1

        if j > i:
            disk[i] = disk[j]
            disk[j] = "."
            j -= 1

    return disk


def calculate_checksum(disk: list) -> int:
    checksum = 0
    for i, block in enumerate(disk):
        if block != ".":
            checksum += i * int(block)
    return checksum


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    disk = parse_disk(input_data)
    disk = compact_disk(disk)
    return calculate_checksum(disk)


def compact_disk_whole_files(disk: list) -> list:
    file_blocks = {}
    free_space_blocks = []

    for i, block in enumerate(disk):
        if block != ".":
            if block not in file_blocks:
                file_blocks[block] = []
            file_blocks[block].append(i)
        else:
            free_space_blocks.append(i)

    file_ids = sorted(file_blocks.keys(), key=int, reverse=True)
    free_space_set = set(free_space_blocks)

    for file_id in file_ids:
        file_positions = file_blocks[file_id]
        file_length = len(file_positions)
        original_start = file_positions[0]

        for i in range(len(free_space_blocks) - file_length + 1):
            start_pos = free_space_blocks[i]
            end_pos = free_space_blocks[i + file_length - 1]

            if end_pos - start_pos == file_length - 1 and start_pos < original_start:
                disk[start_pos:start_pos + file_length] = [file_id] * file_length
                for pos in file_positions:
                    disk[pos] = "."

                free_space_set.difference_update(range(start_pos, start_pos + file_length))
                free_space_set.update(file_positions)
                free_space_blocks = sorted(free_space_set)
                break

    return disk


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    disk = parse_disk(input_data)
    disk = compact_disk_whole_files(disk)
    return calculate_checksum(disk)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 1928
    PART2_EXAMPLE_SOLUTION = 2858

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
