def parse_line(line: str):
    number_list = line.split()
    number_list = list(map(int, number_list))
    return number_list


def algorithm(lines: list[str]) -> int:
    list1 = []
    list2 = []

    for line in lines:
        number1, number2 = parse_line(line)
        list1.append(number1)
        list2.append(number2)

    list1.sort()
    list2.sort()

    total = 0
    for index in range(len(list1)):
        total += abs(list1[index] - list2[index])

    return total


def main():
    with open("day1/aoc1.txt", "r") as file_data:
        data = file_data.readlines()

    total = algorithm(data)
    print(total)


if __name__ == "__main__":
    main()
