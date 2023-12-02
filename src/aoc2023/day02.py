import math
import re

def parse_input(raw_input):
    games = []
    for line in raw_input.split("\n"):
        draws = re.findall(r"([0-9]+) ([a-z]+)", line.split(": ")[1])
        games.append({
            color: max(int(v) for v, k in draws if k == color)
            for color in ("red", "green", "blue")
        })
    return games


def solve_part1(games):
    return sum(
        i for i, max_counts in enumerate(games, start=1)
        if max_counts["red"] <= 12
        and max_counts["green"] <= 13
        and max_counts["blue"] <= 14
    )


def solve_part2(games):
    return sum(math.prod(max_counts.values()) for max_counts in games)
