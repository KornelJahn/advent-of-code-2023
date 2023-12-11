import itertools
import re


def parse_input(raw_input):
    image = raw_input.strip()
    n = raw_input.index("\n") + 1
    galaxies = [to_2d_indices(m.start(), n) for m in re.finditer("#", image)]
    return galaxies


def solve_part1(galaxies):
    return sum_of_distances(expand(galaxies, 2))


def solve_part2(galaxies, factor=1000000):
    return sum_of_distances(expand(galaxies, factor))


def to_2d_indices(flat_idx, row_length):
    return flat_idx // row_length, flat_idx % row_length


def sum_of_distances(galaxies):
    return sum(dist(g1, g2) for g1, g2 in itertools.combinations(galaxies, 2))


def expand(galaxies, factor):
    # The row and column indices of empty empty rows and columns, respectively
    vs, hs = (set(range(len(xs))) - set(xs) for xs in zip(*galaxies))
    c = factor - 1
    return [
        (i + c * sum(v < i for v in vs), j + c * sum(h < j for h in hs))
        for i, j in galaxies
    ]


def dist(g1, g2):
    (i1, j1), (i2, j2) = g1, g2
    return abs(i2 - i1) + abs(j2 - j1)  # Manhattan distance
