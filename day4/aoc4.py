def algorithm(lines: list[str]) -> int:
    word = "XMAS"
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    def is_valid(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])

    def search_from(x, y, dx, dy):
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or lines[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count


def main():
    with open("day4/aoc4.txt", "r") as file_data:
        data = [line.strip() for line in file_data.readlines()]

    total = algorithm(data)
    print(total)


if __name__ == "__main__":
    main()
