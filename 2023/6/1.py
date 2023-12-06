import math
import sys

Input = sys.stdin.read()
lines = Input.split("\n")
time = list(map(int, lines[0].split()[1:]))
distance = list(map(int, lines[1].split()[1:]))


def num_ways(t, d):
    EPS = 0.0000001
    delta = t ** 2 - 4 * (d + EPS)
    u = math.floor((-t - math.sqrt(delta)) / -2)
    l = math.ceil((-t + math.sqrt(delta)) / -2)
    return u - l + 1


# part 1
print("Part 1:", math.prod([num_ways(*w) for w in zip(time, distance)]))
print("Part 2:", num_ways(
    int("".join(lines[0].split()[1:])),
    int("".join(lines[1].split()[1:]))
))

