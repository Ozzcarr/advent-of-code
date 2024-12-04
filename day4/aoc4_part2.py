def mas(lines: list[str], i: int, j: int, reverse=False) -> bool:
    factor = 1 if not reverse else -1
    if lines[i + 1][j + 1 * factor] == "A":
        if lines[i][j] == "M" and lines[i + 2][j + 2 * factor] == "S":
            return True
        elif lines[i][j] == "S" and lines[i + 2][j + 2 * factor] == "M":
            return True

    return False


def algorithm(lines: list[str]) -> int:
    line_len = len(lines[0])
    count = 0

    for i in range(len(lines) - 2):
        for j in range(line_len - 2):
            if mas(lines, i, j) and mas(lines, i, j + 2, reverse=True):
                count += 1

    return count


def main():
    with open("day4/aoc4.txt", "r") as file_data:
        data = file_data.readlines()

    total = algorithm(data)
    print(total)


if __name__ == "__main__":
    main()
