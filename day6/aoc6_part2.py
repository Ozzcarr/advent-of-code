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


def algorithm(map_lines, guard_pos, guard_dir, obstruction=None) -> bool:
    seen_states = set()
    width = len(map_lines[0])
    height = len(map_lines)
    grid = [row[:] for row in map_lines]

    if obstruction:
        row, column = obstruction
        grid[row][column] = "#"

    while (guard_pos, guard_dir) not in seen_states:
        seen_states.add((guard_pos, guard_dir))
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])

        if 0 <= next_pos[1] < width and 0 <= next_pos[0] < height:
            if grid[next_pos[1]][next_pos[0]] != "#":
                guard_pos = next_pos
            else:
                guard_dir = turn_right(guard_dir)
        else:
            return False

    return True


def main():
    with open("day6/aoc6.txt", "r") as file_data:
        data = file_data.read()

    map_lines, guard_pos, guard_dir = parse_input(data)

    total = 0
    for x in range(len(map_lines)):
        for y in range(len(map_lines[0])):
            if map_lines[x][y] != "#" and (x, y) != guard_pos:
                total += algorithm(map_lines, guard_pos, guard_dir, (x, y))

    print(total)


if __name__ == "__main__":
    main()
