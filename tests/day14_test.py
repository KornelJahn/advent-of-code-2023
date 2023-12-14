from pathlib import Path
from aoc2023.day14 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 136
    assert solve_part1(PUZZLE_INPUT) == 103614


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 64
    assert solve_part2(PUZZLE_INPUT) == 83790


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day14.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""")
