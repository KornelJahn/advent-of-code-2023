def parse_input(raw_input):
    images = raw_input.strip().split("\n\n")

    def process_image(image):
        rows = image.split("\n")
        return [[1 if c == "#" else 0 for c in row] for row in rows]

    return list(map(process_image, images))


def solve_part1(images):
    return sum(
        calculate_score(image, calculate_side_length)
        for image in images
    )


def solve_part2(images):
    return sum(
        calculate_score(image, calculate_smudged_side_length)
        for image in images
    )


def calculate_score(image, func):
    score = func(compress(transpose(image)))
    if score:
        return score
    score = 100 * func(compress(image))
    return score


def calculate_side_length(series, exclude=-1):
    for i in range(1, len(series)):
        if i == exclude:
            continue
        if is_mirrored(series, i):
            return i
    return 0


def calculate_smudged_side_length(series):
    original_length = calculate_side_length(series)
    for i in range(len(series)):
        for j in range(i+1, len(series)):
            # Find another number (column) that differs only by one bit and
            # only consider that one
            if count_set_bits(series[i] ^ series[j]) == 1:
                # Smudge only these columns by the other one
                for k in (i, j):
                    smudged_series = series.copy()
                    smudged_series[i] = series[k]
                    smudged_series[j] = series[k]
                    length = calculate_side_length(
                        smudged_series, original_length
                    )
                    if length and length != original_length:
                        return length
    return 0


def transpose(image):
    return [list(col) for col in zip(*image)]


def compress(image):
    return [int("".join(str(i) for i in row), 2) for row in image]


def count_set_bits(n):
    # Brian Kernighan's algorithm
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_mirrored(series, idx):
    s1 = list(reversed(series[:idx]))
    s2 = series[idx:]
    min_len = min(len(s1), len(s2))
    return s1[:min_len] == s2[:min_len]
