from collections import defaultdict
from functools import reduce
import re


def parse_input(raw_input):
    return raw_input.strip().replace("\n", "").split(",")


def solve_part1(seq):
    return sum(hash_(s) for s in seq)


def solve_part2(seq):
    boxes = populate_boxes(seq)
    return sum(
        (box_idx + 1) * slot_idx * fl
        for box_idx, box in boxes.items()
        for slot_idx, (label, fl) in enumerate(box.items(), start=1)
    )


def hash_(s):
    return reduce(lambda v, c: 17 * (v + ord(c)) % 256, s, 0)


def populate_boxes(seq):
    boxes = defaultdict(dict)
    for operation in seq:
        match re.split(r"([=-])", operation):
            case [label, "=", fl_str]:
                boxes[hash_(label)][label] = int(fl_str)
            case [label, "-", _]:
                boxes[hash_(label)].pop(label, None)
    return boxes
