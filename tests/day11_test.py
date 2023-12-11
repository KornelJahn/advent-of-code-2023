from pathlib import Path
from aoc2023.day11 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 374
    assert solve_part1(PUZZLE_INPUT) == 9693756


def test_part2():
    assert solve_part2(EXAMPLE_INPUT, 10) == 1030
    assert solve_part2(EXAMPLE_INPUT, 100) == 8410
    assert solve_part2(PUZZLE_INPUT) == 717878258016


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day11.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""")
