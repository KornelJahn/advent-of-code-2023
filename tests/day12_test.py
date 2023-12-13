from pathlib import Path
from aoc2023.day12 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 21
    assert solve_part1(PUZZLE_INPUT) == 7716


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 525152
    # assert solve_part2(PUZZLE_INPUT) == None


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day12.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""")
