import sys
from functools import lru_cache
from itertools import starmap

def augment(springs, groups):
    return springs + 4 * ('?' + springs), 5 * groups

@lru_cache(maxsize=None)
def backtracking(springs, groups):
    if sum(groups) > len(springs):
        return 0
    if len(groups) == 0:
        if springs.count('#') == 0:
            return 1
        else:
            return 0
    if len(springs) == 0 and not len(groups) == 0:
        return 0
    # skip all the dots
    i = 0
    while springs[i] == '.':
        i += 1
        if i == len(springs):
            return 0
    # check if the group can start at i
    group_end = i + groups[0] - 1
    can_start = group_end < len(springs) and \
        all(s in '?#' for s in springs[i:group_end+1])
    if group_end + 1 < len(springs):
        can_start = can_start and springs[group_end+1] != '#'
    # If there is # at i it has to start
    if springs[i] == '#' and not can_start:
        return 0
    res = 0
    # regular call without starting the group
    if not springs[i] == '#':
        res += backtracking(springs[i+1:], groups)
    # call with starting the group
    if can_start:
        res += backtracking(springs[group_end+2:], groups[1:])
    return res

if __name__ == "__main__":
    data = [line.strip().split() for line in sys.stdin.readlines()]
    processed = [(line[0], tuple(map(int, line[1].split(',')))) for line in data]
    print("Part 1:", sum(starmap(backtracking, processed)))
    augmented = list(starmap(augment, processed))
    print("Part 2:", sum(starmap(backtracking, augmented)))

