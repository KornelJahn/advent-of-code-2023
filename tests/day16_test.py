from pathlib import Path
from aoc2023.day16 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 46
    assert solve_part1(PUZZLE_INPUT) == 8249


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 51
    assert solve_part2(PUZZLE_INPUT) == 8444


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day16.txt").read_text()
)

EXAMPLE_INPUT = parse_input(
r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""")
