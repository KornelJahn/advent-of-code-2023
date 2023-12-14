import copy


def parse_input(raw_input):
    images = raw_input.strip().split("\n\n")
    return [image.split("\n") for image in images]


def solve_part1(images):
    return sum(
        compute_score(image, compute_side_length) for image in images
    )


def solve_part2(images):
    return sum(
        compute_score(image, compute_smudged_side_length) for image in images
    )


def compute_score(image, func):
    score = func(transpose(image))
    if score:
        return score
    score = 100 * func(image)
    return score


def compute_side_length(rows, exclude=-1):
    for i in range(1, len(rows)):
        if i == exclude:
            continue
        if is_mirrored(rows, i):
            return i
    return 0


def compute_smudged_side_length(rows):
    length = compute_side_length(rows)
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            # Find another row that differs only by one element and
            # only consider that one
            if sum(x != y for x, y in zip(rows[i], rows[j])) == 1:
                # Smudge only these columns by the other one
                for k in (i, j):
                    smudged_rows = copy.deepcopy(rows)
                    smudged_rows[i] = rows[k]
                    smudged_rows[j] = rows[k]
                    smudged_length = compute_side_length(smudged_rows, length)
                    if smudged_length and smudged_length != length:
                        return smudged_length
    return 0


def transpose(image):
    return [list(col) for col in zip(*image)]


def is_mirrored(rows, idx):
    s1 = list(reversed(rows[:idx]))
    s2 = rows[idx:]
    min_len = min(len(s1), len(s2))
    return s1[:min_len] == s2[:min_len]
