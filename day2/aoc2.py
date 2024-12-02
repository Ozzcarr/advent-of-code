def parse_line(line: str):
    numbers_str = line.split()
    return list(map(int, numbers_str))


def algorithm(line: str) -> int:
    numbers = parse_line(line)
    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    if not (increasing or decreasing):
        return 0

    valid = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

    return 1 if valid else 0


def main():
    with open("day2/aoc2.txt", "r") as file_data:
        data = file_data.readlines()

    total = 0
    for line in data:
        total += algorithm(line)

    print(total)


if __name__ == "__main__":
    main()
