import re


def algorithm(lines: str) -> int:
    segments = re.split(r"(do\(\)|don't\(\))", lines)
    enabled = True
    total = 0

    for segment in segments:
        if segment == "do()":
            enabled = True
        elif segment == "don't()":
            enabled = False
        elif enabled:
            matches = re.findall(r"mul\((\d+),(\d+)\)", segment)
            total += sum(int(x) * int(y) for x, y in matches)

    return total


def main():
    with open("day3/aoc3.txt", "r") as file_data:
        data = file_data.read()

    total = algorithm(data)
    print(total)


if __name__ == "__main__":
    main()
