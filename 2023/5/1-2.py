import sys
import portion as P
from functools import reduce


def process(phase: str):
    s = phase.split("\n")
    result = []
    for mapping in s[1:]:
        dests, source, n = map(int, mapping.split())
        result.append((P.closed(dests, dests + n - 1),
                       P.closed(source, source + n - 1)))
    return result


def process_interval(seedI):
    for phase in processed:
        new_seedI = P.empty()
        for mapping in phase:
            dest, source = mapping
            intersect = seedI & source
            if intersect:
                seedI = seedI.difference(intersect)
                diff = dest.lower - source.lower
                into = intersect.apply(lambda x: (
                    x.left, x.lower + diff, x.upper + diff, x.right))
                new_seedI = new_seedI.union(into)
        seedI = seedI | new_seedI
    return seedI.lower


data = iter(sys.stdin.read().rstrip().split("\n\n"))
seeds = list(map(int, next(data)[7:].split()))
processed = list(map(process, data))


def union(*args):
    return reduce(lambda a, b: a | b, args)


p1_input = union(*[P.closed(s, s) for s in seeds])
print("Part 1:", process_interval(p1_input))

intervals = [
    P.closed(z[0], z[0] + z[1] + 1) for z in zip(seeds[::2], seeds[1::2])
]
p2_input = union(*intervals)
print("Part 2: ", process_interval(p2_input))
