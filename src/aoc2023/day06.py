import re


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")
    times, distances = (re.findall(r"(\d+)", line) for line in lines)
    return times, distances


def solve_part1(input_):
    times, distances = input_
    # TODO
    return None


def solve_part2(input_):
    times, distances = input_
    return None
