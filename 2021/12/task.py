from collections import defaultdict, deque
from copy import copy

with open("input") as f:
    graph = defaultdict(list)
    for line in f:
        b, e = line.split("-")
        graph[b].append(e.rstrip())
        graph[e.rstrip()].append(b)
        
    count = 0
    radar = deque()
    radar.append({"current": "start", "visited": set()})
    while(radar):
        s = radar[-1]
        radar.pop()
        for c in graph[s["current"]]:
            if c != "start":
                if c == "end":
                    count += 1
                elif c.islower():
                    if c not in s["visited"]:
                        n = {}
                        n["current"] = c
                        n["visited"] = s["visited"]|{c}
                        radar.append(n)
                else:
                    n = {}
                    n["current"] = c
                    n["visited"] = copy(s["visited"])
                    radar.append(n)
    print(count)