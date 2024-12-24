import heapq
import os


def parse_input(input_data: str):
    return input_data.split("\n")


def read_file(filename: str):
    """Reads in the input file."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)
    with open(file_path, "r") as input_file:
        return input_file.read().strip()


def get_neighbors(pos, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for i, (dr, dc) in enumerate(directions):
        new_pos = (pos[0] + dr, pos[1] + dc)
        if grid[new_pos[0]][new_pos[1]] != "#":
            neighbors.append((new_pos, i))
    return neighbors


def bfs(grid, start, end):
    start_pos, start_dir = start
    end_pos = end
    queue = [(0, start_pos, start_dir, [start_pos])]
    visited = {}
    visited[(start_pos, start_dir)] = 0
    best_paths = []

    while queue:
        current_cost, current_pos, current_dir, path = heapq.heappop(queue)

        if current_pos == end_pos:
            if not best_paths or current_cost == best_paths[0][0]:
                best_paths.append((current_cost, path))
            elif current_cost < best_paths[0][0]:
                best_paths = [(current_cost, path)]
            continue

        for neighbor_pos, neighbor_dir in get_neighbors(current_pos, grid):
            new_cost = current_cost + 1
            if neighbor_dir != current_dir:
                new_cost += 1000

            if (neighbor_pos, neighbor_dir) not in visited or new_cost <= visited[(neighbor_pos, neighbor_dir)]:
                visited[(neighbor_pos, neighbor_dir)] = new_cost
                heapq.heappush(queue, (new_cost, neighbor_pos, neighbor_dir, path + [neighbor_pos]))

    best_tiles = set()
    for _, path in best_paths:
        best_tiles.update(path)

    return best_paths[0][0], len(best_tiles)


def part1(input_data: str):
    grid = parse_input(input_data)
    start = None
    end = None

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                start = ((r, c), 0)
            elif char == "E":
                end = (r, c)

    return bfs(grid, start, end)[0]


def part2(input_data: str):
    grid = parse_input(input_data)
    start = None
    end = None

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "S":
                start = ((r, c), 0)
            elif char == "E":
                end = (r, c)

    return bfs(grid, start, end)[1]


def main():
    example_input = read_file("example.txt")
    puzzle_input = read_file("input.txt")

    PART1_EXAMPLE_SOLUTION = 7036
    PART2_EXAMPLE_SOLUTION = 45

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
