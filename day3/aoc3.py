import re

print("P1:", sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", open("day3/aoc3.txt").read())]))
