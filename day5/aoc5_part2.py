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


def sort_update(rules, update):
    position = {num: i for i, num in enumerate(update)}

    for _ in range(len(update)):
        for x, y in rules:
            if x in position and y in position:
                if position[x] > position[y]:
                    position[x], position[y] = position[y], position[x]
                    update[position[x]], update[position[y]] = update[position[y]], update[position[x]]

    return update


def main():
    with open("day5/aoc5.txt", "r") as file_data:
        data = file_data.read()

    rules, updates = parse_input(data)
    incorrect_updates = [update for update in updates if not is_update_correct(rules, update)]
    sorted_updates = [sort_update(rules, update) for update in incorrect_updates]
    total = sum(int(update[len(update) // 2]) for update in sorted_updates)
    print(total)


if __name__ == "__main__":
    main()
