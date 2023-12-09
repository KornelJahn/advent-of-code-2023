from pathlib import Path
from aoc2023.day09 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 114
    assert solve_part1(PUZZLE_INPUT) == 2174807968


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 2
    assert solve_part2(PUZZLE_INPUT) == 1208


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day09.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""")
