from pathlib import Path
from aoc2023.day13 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 405
    assert solve_part1(PUZZLE_INPUT) == 34100


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 400
    assert solve_part2(PUZZLE_INPUT) == 33106


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day13.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""")
