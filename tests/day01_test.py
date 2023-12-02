from pathlib import Path
from aoc2023.day01 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE1_INPUT) == 142
    assert solve_part1(PUZZLE_INPUT) == 53334


def test_part2():
    assert solve_part2(EXAMPLE2_INPUT) == 281
    assert solve_part2(PUZZLE_INPUT) == 52834


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day01.txt").read_text()
)

EXAMPLE1_INPUT = parse_input("""\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""")

EXAMPLE2_INPUT = parse_input("""\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""")
