import sys
import itertools

def expand(galaxies, axis=0, val=1):
    new = []
    xasc = sorted(galaxies, key=lambda x: x[axis])
    last = xasc[0][axis]
    gap = 0
    for galaxy in xasc:
        diff = galaxy[axis] - last
        if diff > 1:
            gap += (diff - 1) * (val - 1)
        last = galaxy[axis]
        if axis == 0:
            new_galaxy = (galaxy[0] + gap, galaxy[1])
        else:
            new_galaxy = (galaxy[0], galaxy[1] + gap)
        new.append(new_galaxy)
    return new


def manhattan(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

def part(galaxies, to_expand):
    expanded = expand(expand(galaxies, 0, to_expand), 1, to_expand)
    return sum(map(manhattan, itertools.combinations(expanded, 2)))

if __name__ == "__main__":
    data = sys.stdin.readlines()
    galaxies = [(x, y) for y, row in enumerate(data) for x, col in enumerate(row) if col == '#']

    print("Part 1:", part(galaxies, 2))
    print("Part2:", part(galaxies, 1000000))
