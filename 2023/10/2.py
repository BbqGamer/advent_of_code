import sys
from copy import deepcopy
from itertools import pairwise


def find(data, char):
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c == char:
                return i, j
    return (-1, -1)


def neighbors(data, x, y, n):
    N = []
    for i in range(max(0, x-n), min(x+n+1, len(data[0])-1)):
        N.append(data[i][max(0, y-n): min(y+n+1, len(data)-1)])
    return N

moves = {
    'F': [(0, 1), (1, 0)],
    '-': [(0, 1), (0, -1)],
    '|': [(1, 0), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    'L': [(0, 1), (-1, 0)],
    '7': [(1, 0), (0, -1)],
}

def iter_cycle(grid, starty, startx):
    curx, cury = startx, starty
    yield curx, cury
    cur = grid[cury][curx]
    dy, dx = moves[cur][0]
    curx += dx
    cury += dy
    while (curx, cury) != (startx, starty):
        yield cury, curx
        cur = grid[cury][curx]
        if moves[cur][0] == (-dy, -dx):
            dy, dx = moves[cur][1]
        else:
            dy, dx = moves[cur][0]
        curx += dx
        cury += dy
    yield cury, curx

contours = {
    'F': [((1, 0), (0, 0), (0, 1))],
    '-': [((0, 0), (0, 1)), ((1, 0), (1, 1))],
    '|': [((0, 0), (1, 0)), ((0, 1), (1, 1))],
    'J': [((0, 1), (1, 1), (1, 0))],
    'L': [((0, 0), (1, 0), (1, 1))],
    '7': [((0, 0), (0, 1), (1, 1))],
}

data = [l.strip() for l in sys.stdin.readlines()]

starty, startx = find(data, 'S')
print(*neighbors(data, starty, startx, 2), sep='\n')

grid = deepcopy(data)
grid[starty] = grid[starty].replace('S', '|')

starty = starty - 1
cycle = iter_cycle(grid, starty, startx)
next(cycle)
y, x = next(cycle)
c1, c2 = contours[grid[y][x]]
C1 = [(y + dy, x + dx) for dy, dx in c1]
C2 = [(y + dy, x + dx) for dy, dx in c2]

for y, x in cycle: 
    for c in contours[grid[y][x]]:
        c_accurate = list(map(lambda p: (y + p[0], x + p[1]), c))
        if c_accurate[0] == C1[-1]:
            C1.extend(c_accurate[1:])
        elif c_accurate[0] == C2[-1]:
            C2.extend(c_accurate[1:])
        elif c_accurate[-1] == C1[-1]:
            C1.extend(reversed(c_accurate[:-1]))
        elif c_accurate[-1] == C2[-1]:
            C2.extend(reversed(c_accurate[:-1]))


def f(pair):
    return (pair[0][0] + pair[1][0]) * (pair[1][1] - pair[0][1])


c1_area = abs(sum(map(f, pairwise(C1)))) // 2
print(c1_area)
c2_area = abs(sum(map(f, pairwise(C2)))) // 2
print(c2_area)
