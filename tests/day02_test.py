from pathlib import Path
from aoc2023.day02 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == None
    # assert solve_part1(PUZZLE_INPUT) == None


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == None
    assert solve_part2(PUZZLE_INPUT) == None


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day02.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")
