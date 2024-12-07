def parse_line(line: str):
    test_value, numbers = line.split(": ")
    return int(test_value), list(map(int, numbers.split()))


def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "|":
            result = int(str(result) + str(numbers[i + 1]))

    return result


def algorithm(line: str) -> int:
    test_value, numbers = parse_line(line)
    from itertools import product
    for operators in product("+*|", repeat=len(numbers) - 1):
        if evaluate(numbers, operators) == test_value:
            return test_value

    return 0


def main():
    with open("day7/aoc7.txt", "r") as file_data:
        data = file_data.readlines()

    total = 0
    for line in data:
        total += algorithm(line)

    print(total)


if __name__ == "__main__":
    main()
