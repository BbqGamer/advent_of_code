from collections import defaultdict, deque

with open("input") as f:
    graph = defaultdict(list)
    for line in f:
        a, b = line.strip().split('-')
        graph[a] += [b]
        graph[b] += [a]

    count = 0
    radar = deque()
    radar.append({"current": "start", "visited": ["start"], "small": False})
    while(radar):
        s = radar[-1]
        radar.pop()
        for c in graph[s["current"]]:
            if c == "end":
                print(s["visited"]+["end"])
                count += 1
                continue
            n = {}
            n["small"] = s["small"]
            if c in s["visited"]:
                if c == "start":
                    continue
                if c.islower():
                    if s["small"] == True:
                        continue
                    else:
                        n["small"] = True
            n["visited"] = s["visited"]+[c]
            n["current"] = c
            radar.append(n)
    print(count)