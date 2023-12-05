from pathlib import Path
from aoc2023.day04 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 13
    assert solve_part1(PUZZLE_INPUT) == 18653


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 30
    assert solve_part2(PUZZLE_INPUT) == 5921508


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day04.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")
