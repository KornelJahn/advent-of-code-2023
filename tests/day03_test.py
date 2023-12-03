from pathlib import Path
from aoc2023.day03 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 4361
    assert solve_part1(PUZZLE_INPUT) == 498559


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 467835
    assert solve_part2(PUZZLE_INPUT) == 72246648


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day03.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")
