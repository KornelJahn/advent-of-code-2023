from pathlib import Path
from aoc2023.day07 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 6440
    assert solve_part1(PUZZLE_INPUT) == 250347426


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 5905
    assert solve_part2(PUZZLE_INPUT) == 251224870


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day07.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""")
