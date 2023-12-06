from pathlib import Path
from aoc2023.day06 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 288
    assert solve_part1(PUZZLE_INPUT) == 861300


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 71503
    assert solve_part2(PUZZLE_INPUT) == 28101347


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day06.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
Time:      7  15   30
Distance:  9  40  200
""")
