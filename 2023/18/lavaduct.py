import sys
from itertools import pairwise

def parse(line):
    s = line.split()
    return (s[0], int(s[1]))


def parse_2(line):
    s = line.split()
    dir = int(s[2][-2])
    dist = int(s[2][2:-2], 16)
    return ("RULD"[dir], dist)


def points(data):
    res = [(0, 0)]
    for (dir, distance) in data:
        x, y = res[-1]
        match dir:
            case "R": res.append((x + distance, y))
            case "L": res.append((x - distance, y))
            case "U": res.append((x, y + distance))
            case "D": res.append((x, y - distance))
    return res


def shoelace(points):
    return abs(sum([x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(points)])) // 2


def dist(p):
    (x1, y1), (x2, y2) = p
    return abs(x1 - x2) + abs(y1 - y2)


def boundary(points):
    return sum(map(dist, pairwise(points)))


if __name__ == "__main__":
    parsers = [parse, parse_2]
    names = ["Part 1:", "Part 2:"]
    data = sys.stdin.readlines()
    for parser, name in zip(parsers, names):
        p = points(map(parser, data))
        print(name, shoelace(p) + boundary(p) // 2 + 1) # Pick's theorem

