"""Advent of Code 2024 - Day 17"""

import os
import re


def parse_input(input_str: str):
    ra, rb, rc, program = re.findall(r": (.*)", input_str)
    return int(ra), int(rb), int(rc), list(map(int, program.split(",")))


def run_program(ra, rb, rc, program):
    output = []
    pc = 0
    while pc < len(program):
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: ra, 5: rb, 6: rc}
        opcode = program[pc]
        operand = program[pc + 1]
        jumped = False
        match opcode:
            case 0:  # adv
                ra >>= combo[operand]
            case 1:  # bxl
                rb ^= operand
            case 2:  # bst
                rb = combo[operand] % 8
            case 3:  # jnz
                if ra != 0:
                    pc = operand
                    jumped = True
            case 4:  # bxc
                rb ^= rc
            case 5:  # out
                output.append(str(combo[operand] % 8))
            case 6:  # bdv
                rb = ra >> combo[operand]
            case 7:  # cdv
                rc = ra >> combo[operand]

        if not jumped:
            pc += 2

    return output


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    return ",".join(run_program(*parse_input(input_data)))


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    _, rb, rc, program = parse_input(input_data)
    valid_a = {0}

    for required_instr in reversed(program):
        next_a = set()

        for a_val in valid_a:
            a_val <<= 3

            for candidate_a in range(a_val, a_val + 8):
                out = run_program(candidate_a, rb, rc, program)
                if out and int(out[0]) == required_instr:
                    next_a.add(candidate_a)

        valid_a = next_a

    return min(valid_a)


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = "4,6,3,5,6,3,5,2,1,0"

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    print("Part 2:", part2(puzzle_input))


if __name__ == "__main__":
    main()
