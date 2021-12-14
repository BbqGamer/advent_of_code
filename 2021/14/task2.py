from collections import Counter, defaultdict

with open("input") as f:
    t, i = f.read()[:-1].split("\n\n")
    instr = dict(l.split(" -> ") for l in i.split("\n"))
    temp = {x: t.count(x) for x in instr.keys()}
    print(temp)
    for step in range(10):
        temp2 = defaultdict(lambda: 0)
        for k in temp.keys():
            n1, n2 = f"{k[0]}{instr[k]}", f"{instr[k]}{k[1]}"
            temp2[n1] += temp[k]
            temp2[n2] += temp[k]
        temp = temp2
    individuals = defaultdict(lambda: 0)
    for k, v in temp2.items():
        individuals[k[0]] += int(v)
        individuals[k[1]] += int(v)
    individuals[t[0]] += 1
    individuals[t[-1]] += 1
    counter = Counter(individuals)
    print(int((max(counter.values()) - min(counter.values()))/2))
