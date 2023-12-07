import sys
from collections import Counter


def ctype(card: str, part2=False) -> int:
    c = Counter(card)
    if part2 and 'J' in c:  # Add Joker count to card with highest count
        j = c['J']
        del c['J']
        if c:
            c[c.most_common(1)[0][0]] += j
        else:
            c['J'] = j

    match (len(c), c.most_common()[0][1]):
        case (5, _):
            return 0
        case (4, _):
            return 1
        case (3, 3):
            return 3
        case (3, _):
            return 2
        case (2, 4):
            return 6
        case (2, _):
            return 5
        case _:
            return 7


m = {str(x): x for x in range(2, 10)}
m.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

hands = [h.split() for h in sys.stdin.readlines()]

part1 = sorted(hands, key=lambda a: (ctype(a[0]), [m[c] for c in a[0]]))
print("part 1:", sum([i * int(h[1]) for i, h in enumerate(part1, 1)]))

m['J'] = 0
part2 = sorted(hands, key=lambda a: (ctype(a[0], True), [m[c] for c in a[0]]))
print("part 1:", sum([i * int(h[1]) for i, h in enumerate(part2, 1)]))
