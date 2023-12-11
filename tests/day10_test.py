from pathlib import Path
from aoc2023.day10 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE1_INPUT) == 8
    assert solve_part1(PUZZLE_INPUT) == 6831


def test_part2():
    assert solve_part2(EXAMPLE2_INPUT) == 10
    assert solve_part2(PUZZLE_INPUT) == 305


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day10.txt").read_text()
)

EXAMPLE1_INPUT = parse_input("""\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""")


EXAMPLE2_INPUT = parse_input("""\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""")
