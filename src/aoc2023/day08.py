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
    nodes = [[node for node in network.keys() if node.endswith("A")]]
    counts = []
    for i in range(2):
        counts.append([])
        nodes.append([])

        for node in nodes[-2]:
            iterator = walk(
                directions,
                network,
                start=node,
                stop_pred=lambda s: s.endswith("Z")
            )
            for count, final_node in enumerate(iterator, start=1):
                pass
            counts[-1].append(count)
            nodes[-1].append(final_node)

        if i > 0:
            # Verify assumptions based on input data observation
            # Verify if counts have a fixed period
            assert counts[-1] == counts[-2]
            # Verify if starting from a final node returns to the same one
            assert nodes[-1] == nodes[-2]

    return math.lcm(*counts[-1])


def walk(directions, network, start, stop_pred):
    node = start
    for direction in itertools.cycle(directions):
        node = network[node][direction]
        yield node
        if stop_pred(node):
            break
