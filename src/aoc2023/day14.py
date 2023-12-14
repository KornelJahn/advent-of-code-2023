from itertools import product


TARGETS = dict(
    N=lambda i, j: (i - 1, j),
    E=lambda i, j: (i, j + 1),
    S=lambda i, j: (i + 1, j),
    W=lambda i, j: (i, j - 1),
)
GRID_ITERS = dict(
    N=lambda m, n: product(range(m), range(n)),
    E=lambda m, n: (
        reversed(t) for t in product(reversed(range(n)), range(m))
    ),
    S=lambda m, n: product(reversed(range(m)), range(n)),
    W=lambda m, n: (reversed(t) for t in product(range(n), range(m))),
)


def parse_input(raw_input):
    rows = raw_input.strip().split("\n")
    platform = [list(row) for row in rows]
    return platform


def solve_part1(platform):
    platform = next(iter(move(platform)))
    return compute_load(platform)


def solve_part2(platform):
    target_cycles = 1000000000
    offset = 200
    sample_count = 400
    load_samples = [
        compute_load(platform)
        for i, platform in
        enumerate(move(platform, cycle="NWSE", max_count=sample_count))
    ]
    period = find_period(load_samples[offset:])
    return load_samples[offset - 1 + (target_cycles - offset) % period]


def step(platform, direction):
    # Side-effect warning: inplace platform changes
    m, n = len(platform), len(platform[0])
    for i, j in GRID_ITERS[direction](m, n):
        if platform[i][j] != "O":
            continue
        k, l = i, j
        while True:
            p, q = TARGETS[direction](k, l)
            if 0 <= p < m and 0 <= q < n and platform[p][q] == ".":
                k, l = p, q
            else:
                break
        platform[i][j] = "."
        platform[k][l] = "O"


def move(platform, cycle="N", max_count=1):
    # Side-effect warning: inplace platform changes
    for _ in range(max_count):
        for direction in cycle:
            step(platform, direction)
        yield platform


def compute_load(platform):
    n = len(platform)
    return sum((n - i) * row.count("O") for i, row in enumerate(platform))


def find_period(seq, min_length=5):
    for i in range(min_length, len(seq)//2):
        for j in range(i):
            if seq[j] != seq[i + j]:
                break
        else:
            return i
