from pathlib import Path
from aoc2023.day10 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 8
    assert solve_part1(PUZZLE_INPUT) == None


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == None
    assert solve_part2(PUZZLE_INPUT) == None


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day10.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""")
