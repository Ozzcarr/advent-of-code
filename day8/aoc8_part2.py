from itertools import permutations


def parse_input(lines: list[str]):
    antennas = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char.isalnum():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas


def algorithm(grid, antennas) -> int:
    positions = set()

    for frequency in antennas.keys():
        for (r1, c1), (r2, c2) in permutations(antennas[frequency], 2):
            dr = r2 - r1
            dc = c2 - c1
            n = 1
            while 0 <= r1 + n * dr < len(grid) and 0 <= c1 + n * dc < len(grid[0]):
                positions.add((r1 + n * dr, c1 + n * dc))
                n += 1

    return len(positions)


def main():
    with open("day8/aoc8.txt", "r") as file_data:
        data = file_data.read().split("\n")

    antennas = parse_input(data)
    total = algorithm(data, antennas)
    print(total)


if __name__ == "__main__":
    main()
