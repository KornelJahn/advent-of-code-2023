from pathlib import Path
from aoc2023.day15 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 1320
    # assert solve_part1(PUZZLE_INPUT) == None


def test_part2():
    pass
    # assert solve_part2(EXAMPLE_INPUT) == None
    # assert solve_part2(PUZZLE_INPUT) == None


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day15.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""")
