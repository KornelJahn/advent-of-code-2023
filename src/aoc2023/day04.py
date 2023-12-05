def parse_input(raw_input):
    lines = raw_input.strip().split("\n")

    def count_wins(line):
        winning, own = (s.split() for s in line.split(":")[1].split("|"))
        return len(set(winning) & set(own))

    return [count_wins(line) for line in lines]


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
    if node[0] == 0:
        return []
    return [node[i:] for i in range(1, node[0] + 1)]
