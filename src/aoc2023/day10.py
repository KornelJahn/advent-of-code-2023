L, R, U, D = (0, -1), (0, 1), (-1, 0), (1, 0)
TILES = {
    "|": {U: U, D: D}, "-": {L: L, R: R},
    "L": {D: R, L: U}, "J": {D: L, R: U},
    "7": {U: L, R: D}, "F": {U: R, L: D},
}
STARTERS = {frozenset(dirmap.values()): tile for tile, dirmap in TILES.items()}


def parse_input(raw_input):
    raw_input = raw_input.strip()
    map_ = [list(row) for row in raw_input.strip().split("\n")]
    i0, j0 = to_2d_indices(raw_input.index("S"), len(map_[0]) + 1)
    map_[i0][j0] = find_out_tile(map_, i0, j0)
    return map_, i0, j0


def solve_part1(input_):
    path = trace_path(*input_)
    return len(path) // 2


def solve_part2(input_):
    map_, i0, j0 = input_
    boundary = set(trace_path(map_, i0, j0))
    area_counter = 0
    for i, row in enumerate(map_):
        for j, tile in enumerate(row):
            if (i, j) in boundary:
                continue
            isect_count = sum(
                1 for k in range(j+1, len(row))
                if (i, k) in boundary and row[k] in "|F7"
            )
            if isect_count % 2 == 1:
                area_counter += 1
    return area_counter


def to_2d_indices(flat_idx, row_length):
    return flat_idx // row_length, flat_idx % row_length


def find_out_tile(map_, i, j):
    return STARTERS[
        frozenset(
            vec for vec in (L, U, R, D) if
            step(map_, i, j, *vec)[2] is not None
        )
    ]


def trace_path(map_, i0, j0):
    tile = get_tile(map_, i0, j0)
    p0, q0 = next(iter(TILES[tile].values()))
    return [(i, j) for i, j in walk(map_, i0, j0, p0, q0)]


def get_tile(map_, i, j):
    if 0 <= i < len(map_) and 0 <= j < len(map_[0]):
        return map_[i][j]
    else:
        return "."


def walk(map_, i0, j0, p0, q0):
    i, j, p, q = i0, j0, p0, q0
    while True:
        i, j, p, q = step(map_, i, j, p, q)
        yield i, j
        if (i == i0 and j == j0) or p is None:
            break


def step(map_, i, j, p, q):
    i, j = i + p, j + q
    tile = get_tile(map_, i, j)
    try:
        p, q = TILES[tile][p, q]
    except KeyError:
        p, q = None, None
    return i, j, p, q
