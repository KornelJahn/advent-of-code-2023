def parse_input(raw_input):
    lines = raw_input.strip().split("\n")

    def count_wins(line):
        winning, own = (s.split() for s in line.split(":")[1].split("|"))
        return len(set(winning) & set(own))

    return [count_wins(line) for line in lines]


def solve_part1(win_counts):
    def points(count):
        return 2**(count - 1) if count > 0 else 0

    return sum(points(win_count) for win_count in win_counts)


def solve_part2(win_counts):
    card_counts = [1 for _ in win_counts]
    for i, n in enumerate(win_counts):
        for j in range(n):
            try:
                card_counts[i + j + 1] += card_counts[i]
            except IndexError:
                pass
    return sum(card_counts)
