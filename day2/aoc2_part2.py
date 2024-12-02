def parse_line(line: str):
    numbers_str = line.split()
    return list(map(int, numbers_str))


def is_valid(numbers: list[int]) -> bool:
    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    if not (increasing or decreasing):
        return False

    valid = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

    return valid


def algorithm(line: str) -> int:
    numbers = parse_line(line)

    if is_valid(numbers):
        return 1

    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i + 1:]
        if is_valid(modified_numbers):
            return 1

    return 0


def main():
    with open("day2/aoc2.txt", "r") as file_data:
        data = file_data.readlines()

    total = 0
    for line in data:
        total += algorithm(line)

    print(total)


if __name__ == "__main__":
    main()
