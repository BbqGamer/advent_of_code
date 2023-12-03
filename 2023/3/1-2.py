import sys
from collections import defaultdict


def is_symbol(c) -> bool:
    return not c.isdigit() and c != "."


if __name__ == "__main__":
    data = ['.' + l.strip() + '.' for l in sys.stdin]
    data.insert(0, '.' * len(data[0]))
    data.append('.' * len(data[0]))

    gears = defaultdict(list)
    part1 = 0

    for i in range(1, len(data)-1):
        start = -1
        num_started = False
        for j in range(1, len(data[0])):
            cur = data[i][j]
            if cur.isdigit() and not num_started:
                num_started = True
                start = j
            elif not cur.isdigit() and num_started:
                num_started = False
                num = int(data[i][start:j])

                neighbors = {
                    (x,y) for x in [i-1, i+1] for y in range(start-1, j+1)
                } | {(i, start-1), (i, j)}
                
                G = []
                is_part = False
                for (x,y) in neighbors:
                    if is_symbol(data[x][y]):
                        is_part = True

                    if data[x][y] == "*":
                        G.append((x,y))
                
                if is_part:
                    part1 += num
                    for g in G:
                        gears[g].append(num)

    part2 = 0
    for gear in gears.values():
        if len(gear) == 2:
            part2 += gear[0] * gear[1]

    print("Part1: ", part1)
    print("Part2: ", part2)

