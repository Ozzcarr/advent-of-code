"""Advent of Code 2024 - Day 24"""

import os
from graphlib import TopologicalSorter


def parse_input(input_data: str) -> tuple:
    gates, operations = input_data.split("\n\n")
    gates_dict = {}
    for gate in gates.split("\n"):
        inpt, outpt = gate.split(": ")
        gates_dict[inpt] = int(outpt)

    op_order = {}
    op_indices = {}
    for idx, operation in enumerate(operations.split("\n")):
        ops = operation.split()
        op_order[ops[4]] = {ops[0], ops[2]}
        op_indices[ops[4]] = idx

    sorted_ops = tuple(TopologicalSorter(op_order).static_order())
    sorted_indices = [op_indices[op] for op in sorted_ops if op in op_indices]
    return gates_dict, operations, sorted_indices


def generate_graphviz_dot(input_data: str, filename="2024/day24/graph.dot"):
    operations = input_data.split("\n\n")[1]
    dot_lines = ["digraph G {", "    rankdir=LR;", ""]
    colors = {"AND": "red", "OR": "green", "XOR": "blue"}
    for operation in operations.split("\n"):
        ops = operation.split()
        dot_lines.append(f'    "{ops[0]}" -> "{ops[4]}" [color={colors[ops[1]]}];')
        dot_lines.append(f'    "{ops[2]}" -> "{ops[4]}" [color={colors[ops[1]]}];')
    dot_lines.append("}")

    with open(filename, "w") as f:
        f.write("\n".join(dot_lines))


def execute_operation(gates, operations, index):
    row = operations.split("\n")[index]
    x1, op, x2, _, y = row.split()

    if op == "AND":
        gates[y] = gates[x1] and gates[x2]
    elif op == "OR":
        gates[y] = gates[x1] or gates[x2]
    elif op == "XOR":
        gates[y] = gates[x1] ^ gates[x2]


def part1(input_data: str):
    """Solve part 1 of the puzzle."""
    gates, operations, row_order = parse_input(input_data)

    for row in row_order:
        execute_operation(gates, operations, row)

    idx = 0
    outpt = "z00"
    num = ""
    while outpt in gates:
        num = str(gates[outpt]) + num
        idx += 1
        outpt = "z{:02d}".format(idx)

    return int(num, 2)


def part2(input_data: str):
    """Solve part 2 of the puzzle."""
    # Pair 1: cmv, z17
    # Pair 2: rmj, z23
    # Pair 3: rdg, z30
    # Pair 4: btb, mwp vid x38 och y38
    solution = ["cmv", "z17", "rmj", "z23", "rdg", "z30", "btb", "mwp"]
    return ",".join(sorted(solution))


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 2024

    part1_example_solution = part1(example_input)
    if part1_example_solution == PART1_EXAMPLE_SOLUTION:
        print("Part 1:", part1(puzzle_input))
    else:
        print(f"Part 1 Failed: {part1_example_solution} != {PART1_EXAMPLE_SOLUTION}")

    print("Part 2:", part2(puzzle_input))


if __name__ == "__main__":
    main()
