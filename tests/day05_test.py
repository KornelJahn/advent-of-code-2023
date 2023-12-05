from pathlib import Path
from aoc2023.day05 import parse_input, solve_part1, solve_part2


def test_part1():
    assert solve_part1(EXAMPLE_INPUT) == 35
    assert solve_part1(PUZZLE_INPUT) == 289863851


def test_part2():
    assert solve_part2(EXAMPLE_INPUT) == 46
    assert solve_part2(PUZZLE_INPUT) == 60568880


PUZZLE_INPUT = parse_input(
    (Path(__file__).parent / "data" / "day05.txt").read_text()
)

EXAMPLE_INPUT = parse_input("""\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""")
