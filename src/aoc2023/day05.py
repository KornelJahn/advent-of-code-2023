from functools import reduce
import re

try:
    from itertools import batched
except:
    from itertools import islice

    # https://docs.python.org/3/library/itertools.html#itertools.batched
    def batched(iterable, n):
        # batched('ABCDEFG', 3) --> ABC DEF G
        if n < 1:
            raise ValueError('n must be at least one')
        it = iter(iterable)
        while batch := tuple(islice(it, n)):
            yield batch


def parse_input(raw_input):
    seed_data, *rules = (
        [int(s) for s in re.findall(r"(\d+)", s)]
        for s in raw_input.split("-to-")
    )
    all_breakpoints = []
    for rule in rules:
        default = {0: 0}
        lower = {}
        upper = {}
        for dst_start, src_start, length in batched(rule, 3):
            lower[src_start] = dst_start
            upper[src_start + length] = src_start + length
        bpts = dict(sorted((default | upper | lower).items()))
        all_breakpoints.append(bpts)
    return seed_data, all_breakpoints


def solve_part1(input_):
    seeds, breakpoints = input_
    return min(
        reduce(lambda seed, bpts: map_value(bpts, seed), breakpoints, seed)
        for seed in seeds
    )


def solve_part2(input_):
    seed_ranges, breakpoints = input_
    intervals = [
        (src_start, src_start+length-1)
        for src_start, length in batched(seed_ranges, 2)
    ]
    output_intervals = reduce(
        lambda ivals, bpts: map_intervals(bpts, ivals),
        breakpoints,
        intervals
    )
    return min(lo for lo, _ in output_intervals)


def map_value(breakpoints, n):
    for i, j in reversed(breakpoints.items()):
        if n >= i:
            return j + (n - i)


def map_intervals(breakpoints, intervals):
    input_intervals = []
    for a, b in intervals:
        new_bpts = (
            [a] +
            [x for x in breakpoints.keys() if x > a and x < b] +
            [b]
        )
        input_intervals += [(c, d-1) for c, d in zip(new_bpts, new_bpts[1:])]
    output_intervals = [
        (map_value(breakpoints, c), map_value(breakpoints, d))
        for c, d in input_intervals
    ]
    return output_intervals
