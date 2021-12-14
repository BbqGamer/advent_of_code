from collections import Counter, defaultdict

def countDifference(temp):
    i = defaultdict(lambda: 0)
    for k, v in temp2.items():
        i[k[0]] += int(v)
        i[k[1]] += int(v)
    i[t[0]] += 1
    i[t[-1]] += 1
    counter = Counter(i)
    return int((max(counter.values()) - min(counter.values()))/2)

with open("input") as f:
    t, i = f.read()[:-1].split("\n\n")
    instr = dict(l.split(" -> ") for l in i.split("\n"))
    temp = {x: t.count(x) for x in instr.keys()}
    for step in range(40):
        temp2 = defaultdict(lambda: 0)
        for k in temp.keys():
            n1, n2 = f"{k[0]}{instr[k]}", f"{instr[k]}{k[1]}"
            temp2[n1] += temp[k]
            temp2[n2] += temp[k]
        temp = temp2
        if step == 9:
            print("Part 1: ", countDifference(temp))
    print("Part 2: ", countDifference(temp))