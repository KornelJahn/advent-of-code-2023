from collections import defaultdict

ELEMENTS = {
    ".": lambda vx, vy: {(vx, vy)},
    "/": lambda vx, vy: {(vy, vx)},
    "\\": lambda vx, vy: {(-vy, -vx)},
    "|": lambda vx, vy: {(0, vy + vx*vx), (0, vy - vx*vx)},
    "-": lambda vx, vy: {(vx + vy*vy, 0), (vx - vy*vy, 0)},
}


def parse_input(raw_input):
    rows = raw_input.strip().split("\n")
    return rows


def solve_part1(rows):
    return count_energized(rows, (0, 0, 1, 0))


def solve_part2(rows):
    xmax, ymax = len(rows[0]) - 1, len(rows) - 1
    initial_states = (
        [(0, y, 1, 0) for y in range(-ymax, 1)]
        + [(xmax, y, -1, 0) for y in range(-ymax, 1)]
        + [(x, 0, 0, -1) for x in range(0, xmax + 1)]
        + [(x, ymax, 0, 1) for x in range(0, xmax + 1)]
    )
    return max(count_energized(rows, state) for state in initial_states)


def count_energized(rows, initial_state):
    energized = defaultdict(set)
    xmax, ymax = len(rows[0]) - 1, len(rows) - 1
    stack = [initial_state]
    while stack:
        x, y, vx, vy = stack.pop()
        if (vx, vy) in energized.get((x, y), set()):
            continue
        energized[x, y].add((vx, vy))
        for vx, vy in ELEMENTS[rows[-y][x]](vx, vy):
            xp = x + vx
            yp = y + vy
            if 0 <= xp <= xmax and -ymax <= yp <= 0:
                stack.append((xp, yp, vx, vy))
    return len(energized)
