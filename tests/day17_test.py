from pathlib import Path
from aoc2023.day17 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 102
    # assert solve_part1(PUZZLE_INPUT) == None


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == None
    assert solve_part2(PUZZLE_INPUT) == None


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day17.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""")
