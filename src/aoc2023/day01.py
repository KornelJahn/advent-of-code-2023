from functools import partial
import re
import string

ALPHA_DIGITS = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]

TABLE = (
    {s: i for i, s in enumerate(string.digits)}
    | {s: i for i, s in enumerate(ALPHA_DIGITS)}
)


def parse_input(raw_input):
    return raw_input.strip().split()


def solve_part1(lines):
    pattern = "|".join(string.digits)
    return sum(map(partial(extract_number, pattern), lines))


def solve_part2(lines):
    pattern = "|".join(string.digits) + "|" + "|".join(ALPHA_DIGITS)
    return sum(map(partial(extract_number, pattern), lines))


def extract_number(pattern, line):
    front = TABLE[re.search(f"({pattern})", line).group(0)]
    rear = TABLE[re.search(f"({pattern[::-1]})", line[::-1]).group(0)[::-1]]
    return 10 * front + rear
