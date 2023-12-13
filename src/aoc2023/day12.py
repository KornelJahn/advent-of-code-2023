import itertools


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")

    def convert(line):
        head, tail = line.split(" ")
        group_sizes = list(map(int, tail.split(",")))
        return head, group_sizes

    return list(map(convert, lines))


def solve_part1(input_):
    return sum(
        arrangement_count(*process_record(record), group_sizes)
        for record, group_sizes in input_
    )


def solve_part2(input_):
    counts = []
    for n in (1, 2):
        counts.append([
            arrangement_count(
                *process_record("?".join(itertools.repeat(record, n))),
                group_sizes * n
            )
            for record, group_sizes in input_
        ])
    return sum(m * (n // m)**4 for m, n in zip(*counts))


def process_record(record):
    bits = 0
    wildcards = []
    for i, c in enumerate(record):
        if c == "#":
            bits |= 1 << i
        elif c == "?":
            wildcards.append(i)
    return bits, wildcards


# Naive approach
def arrangement_count(bits, wildcards, group_sizes):
    remaining = sum(group_sizes) - count_1(bits)
    return sum(
        count_groups_of_1(set_1(bits, *positions)) == group_sizes
        for positions
        in itertools.combinations(wildcards, remaining)
    )


# def arrangement_count(bits, wildcards, group_sizes):
#     remaining = sum(group_sizes) - count_1(bits)
#     return sum(
#         1 for _ in candidates(bits, wildcards, remaining, group_sizes)
#     )


# def candidates(bits, wildcards, remaining, group_sizes):
#     if not remaining:
#         if count_groups_of_1(bits) == group_sizes:
#             yield bits
#         return
#     else:
#         for i in range(len(wildcards)):
#             new_bits = set_1(bits, wildcards[i])
#             if count_groups_of_1(
#                 truncate(new_bits, wildcards[i]+1)
#             ) > group_sizes:
#                 continue
#             yield from candidates(
#                 new_bits, wildcards[i+1:], remaining - 1, group_sizes
#             )


def set_1(bits, *positions):
    for i in positions:
        bits |= 1 << i
    return bits


def count_groups_of_1(bits):
    groups = []
    cnt = 0
    while bits:
        lsb = bits & 1
        if lsb:
            cnt += 1
        else:
            if cnt > 0:
                groups.append(cnt)
            cnt = 0
        bits >>= 1
    if cnt > 0:
        groups.append(cnt)
    return groups


def count_1(bits):
    # Brian Kerninghan's algorithm
    cnt = 0
    while bits:
        bits &= bits - 1
        cnt += 1
    return cnt


def truncate(bits, n):
    return bits & (1 << n - 1)
