import itertools
import math
import re


def parse_input(raw_input):
    directions, map_ = raw_input.strip().split("\n\n")
    parsed_nodes = [
        re.findall(r"([0-9A-Z]+)", line) for line in map_.split("\n")
    ]
    network = {k: {"L": l, "R": r} for k, l, r in parsed_nodes}
    return directions, network


def solve_part1(input_):
    directions, network = input_
    return sum(1 for _ in walk(
        directions, network, start="AAA", stop_pred=lambda s: s == "ZZZ"
    ))


def solve_part2(input_):
    directions, network = input_
    counts_to_first_stop = []
    first_stops = []
    for start in [node for node in network.keys() if node.endswith("A")]:
        iterator = walk(
            directions,
            network,
            start,
            stop_pred=lambda s: s.endswith("Z")
        )
        for count, node in enumerate(iterator, start=1):
            pass
        counts_to_first_stop.append(count)
        first_stops.append(node)

    period_counts = []
    for start in first_stops:
        iterator = walk(
            directions,
            network,
            start,
            stop_pred=lambda s: s.endswith("Z")
        )
        period_counts.append(sum(1 for _ in iterator))

    assert counts_to_first_stop == period_counts

    return math.lcm(*period_counts)


def walk(directions, network, start, stop_pred):
    node = start
    for direction in itertools.cycle(directions):
        node = network[node][direction]
        yield node
        if stop_pred(node):
            break
