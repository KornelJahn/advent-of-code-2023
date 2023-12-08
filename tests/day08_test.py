from pathlib import Path
from aoc2023.day08 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE1_INPUT) == 2
    assert solve_part1(PUZZLE_INPUT) == 14681


def test_part2():
    assert solve_part2(EXAMPLE2_INPUT) == 6
    assert solve_part2(PUZZLE_INPUT) == 14321394058031


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day08.txt").read_text()
)

EXAMPLE1_INPUT = parse_input("""\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""")

EXAMPLE2_INPUT = parse_input("""\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""")
