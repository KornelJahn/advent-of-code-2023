from collections import defaultdict


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")
    cards = [
        [group.split() for group in line.split(": ")[1].split(" | ")]
        for line in lines
    ]
    win_counts = [
        len(set(winning).intersection(mine)) for winning, mine in cards
    ]
    return win_counts


def solve_part1(win_counts):
    return sum(points(win_count) for win_count in win_counts)


def solve_part2(win_counts):
    tree = [len(win_counts)] + win_counts
    return sum(1 for node in preorder_dfs(tree))


def points(count):
    return 2**(count - 1) if count > 0 else 0


def preorder_dfs(tree):
    for node in children(tree):
        yield node
        yield from preorder_dfs(node)


def children(node):
    if not node or node[0] == 0:
        return []
    return [node[i:] for i in range(1, node[0] + 1)]
