import math
import re


def parse_input(raw_input):
    line_length = raw_input.index("\n")
    numbers = [
        (
            int(m.group()),
            to_row_col_indices(m.start(0), line_length + 1),
            len(m.group())
        )
        for m in re.finditer(r"(\d+)", raw_input)
    ]
    symbols = [
        (
            m.group(),
            to_row_col_indices(m.start(0), line_length + 1)
        )
        for m in re.finditer(r"([^\d\.\r\n])", raw_input)
    ]
    return numbers, symbols


def solve_part1(input_):
    numbers, symbols = input_
    return sum(n[0] for n in numbers if any(adjacent(n, s) for s in symbols))


def solve_part2(input_):
    numbers, symbols = input_
    return sum(gear_ratio(s, numbers) for s in symbols if s[0] == "*")


def to_row_col_indices(flat_index, line_length):
    return flat_index // line_length, flat_index % line_length


def adjacent(number, symbol):
    _, (i, j), n = number
    _, (p, q) = symbol
    return i-1 <= p <= i+1 and j-1 <= q <= j+n


def gear_ratio(symbol, numbers):
    neighbors = [n[0] for n in numbers if adjacent(n, symbol)]
    return math.prod(neighbors) if len(neighbors) == 2 else 0
