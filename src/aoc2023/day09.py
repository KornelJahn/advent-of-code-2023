import re

def parse_input(raw_input):
    lines = raw_input.strip().split("\n")

    def convert(line):
        return [int(d) for d in re.findall(r"(-?\d+)", line)]

    return list(map(convert, lines))


def solve_part1(multi_series):
    return sum(extrapolate(xs) for xs in multi_series)


def solve_part2(multi_series):
    return sum(extrapolate(list(reversed(xs))) for xs in multi_series)


# Recurrence relation for an arbitrary element of the triangle:
# a[i,j] = a[i-1,j+1] - a[i-1,j]
#
# Diagonal elements:
# a[0,n] = a[1,n-1] + a[0,n-1]
# a[1,n-1] = a[2,n-2] + a[1,n-2]
# a[2,n-2] = a[3,n-3] + a[2,n-3]
# ...
# a[n,0] = 0 (by definition)
#
# Expanding all intermediate extrapolated elements a[i,n-i]:
# a[0,n] = a[2,n-2] + a[1,n-2] + a[0,n-1]
#        = a[3,n-3] + a[2,n-3] + a[1,n-2] + a[0,n-1]
#        = ...
#        = a[n,0] + a[n-1,0] + a[n-2,1] + a[n-3,2] + ...
#        = a[n-1,0] + a[n-2,1] + a[n-3,2] + ...
#
# In summary, the extrapolated value is simply the sum of diagonal elements.


# def extrapolate(xs, acc=0):
#     if all(x == 0 for x in xs):
#         return acc
#     else:
#         return extrapolate([y - x for y, x in zip(xs[1:], xs)], acc + xs[-1])


# Manual tail-call optimization
def extrapolate(xs):
    acc = 0
    while True:
        acc += xs[-1]
        xs = [y - x for y, x in zip(xs[1:], xs)]
        if all(x == 0 for x in xs):
            return acc
