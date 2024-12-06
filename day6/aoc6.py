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


def algorithm(map_lines, guard_pos, guard_dir) -> int:
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


def main():
    with open("day6/aoc6.txt", "r") as file_data:
        data = file_data.read()

    map_lines, guard_pos, guard_dir = parse_input(data)
    total = algorithm(map_lines, guard_pos, guard_dir)
    print(total)


if __name__ == "__main__":
    main()
