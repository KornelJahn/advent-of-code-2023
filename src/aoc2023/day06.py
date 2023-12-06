import math
import re


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")
    total_times, min_distances = (re.findall(r"(\d+)", line) for line in lines)
    return total_times, min_distances


def solve_part1(input_):
    total_times, min_distances = map(lambda xs: map(int, xs), input_)
    return math.prod(
        outcome_count(t_max, d_min)
        for t_max, d_min in zip(total_times, min_distances)
    )


def solve_part2(input_):
    t_max, d_min = map(lambda xs: int("".join(xs)), input_)
    return outcome_count(t_max, d_min)


# Derivation of the formula for the outcome count limits:
#
# If holding the button lasts for time `t`, then the gained velocity is
#
# v = a t,
#
# where a = 1 mm/ms^2. The distance covered afterwards is then
#
# d = v (t_max - t),
#
# where `t_max` is the total time. Expanding:
#
# d = - a t^2 + a t_max t,
#
# which needs to be greater than some minimal distance `d_min`, therefore we
# seek integer times between the roots of the quadratic polynomial
#
# d - d_min = -a t^2 + a t_max t - d_min,
#
# given by
#
# t_1/2 = t_max/2 +/- 1/2 sqrt(a^2 t_max^2 - 4 a d_min)


def outcome_count(t_max, d_min):
    a = 1.0  # mm/ms^2
    sqrt_D = math.sqrt(a**2 * t_max**2 - 4 * a * d_min)
    t1 = 0.5*(t_max - sqrt_D)
    t2 = 0.5*(t_max + sqrt_D)
    return math.ceil(t2) - (math.floor(t1) + 1)
