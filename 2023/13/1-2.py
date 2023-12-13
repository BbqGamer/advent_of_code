import sys
import numpy as np

def find_mirrors(pattern):
    mirrors = []
    for i in range(1, pattern.shape[1]):
        x1 = i-1
        x2 = i
        while np.all(pattern[:,x1] == pattern[:,x2]):
            x1 -= 1
            x2 += 1
            if x1 < 0 or x2 >= pattern.shape[1]:
                mirrors.append(i)
                break
    return mirrors

def parse(data):
    return [
        np.array([list(map(lambda a: 1 if a == '#' else 0, list(l.strip()))) for l in p])
        for p in [l.split() for l in data.split('\n\n')]
    ]

def part1(patterns):
    mirrors = []
    for pat in patterns:
        M = find_mirrors(pat)
        if M:
            mirrors.append((M[0], 1))
        else:
            M = find_mirrors(pat.T)
            assert M 
            mirrors.append((M[0], 0))
    return mirrors

def pattern_alterations(pattern):
    for i in range(pattern.shape[0]):
        for j in range(pattern.shape[1]):
            new_pattern = pattern.copy()
            new_pattern[i,j] = 1 - new_pattern[i,j]
            yield new_pattern

def part2(patterns, mirrors):
    new_mirrors = []
    for i, pat in enumerate(patterns):
        m, axis = mirrors[i]
        found = False
        for altered in pattern_alterations(pat):
            if found:
                break
            vertical = find_mirrors(altered)
            for v in vertical:
                if axis != 1 or v != m:
                    new_mirrors.append((v, 1))
                    found = True
                    break

            horizontal = find_mirrors(altered.T)
            for h in horizontal:
                if axis != 0 or h != m:
                    new_mirrors.append((h, 0))
                    found = True
                    break
    return new_mirrors 

def sum_mirrors(mirrors):
    return sum(map(lambda m: m[0] if m[1] == 1 else m[0] * 100, mirrors))

if __name__ == '__main__':
    data = sys.stdin.read()
    patterns = parse(data)
    mirrors = part1(patterns)
    print("Part 1:", sum_mirrors(mirrors))
    fixed_mirrors = part2(patterns, mirrors)
    print("Part 2:", sum_mirrors(fixed_mirrors))


INPUT_EXAMPLE = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def test_parts():
    patterns = parse(INPUT_EXAMPLE)
    mirrors = part1(patterns)
    assert sum_mirrors(mirrors) == 405
    fixed_mirrors = part2(patterns, mirrors)
    assert sum_mirrors(fixed_mirrors) == 400

