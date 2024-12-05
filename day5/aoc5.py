import re


def parse_input(input_str: str):
    rules = re.findall(r"(\d+)\|(\d+)", input_str)
    updates = [update.split(",") for update in input_str.split("\n\n")[1].split("\n")]
    return rules, updates


def is_update_correct(rules, update):
    for x, y in rules:
        if x in update and y in update:
            if int(update.index(x)) > int(update.index(y)):
                return False
    return True


def main():
    with open("day5/aoc5.txt", "r") as file_data:
        data = file_data.read()

    rules, updates = parse_input(data)
    correct_updates = [update for update in updates if is_update_correct(rules, update)]
    total = sum(int(update[len(update) // 2]) for update in correct_updates)
    print(total)


if __name__ == "__main__":
    main()
