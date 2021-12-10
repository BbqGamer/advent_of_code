import collections

c = {x:i for i,x in enumerate(["(","[","{","<",")","]","}",">"])}
p = [3, 57, 1197, 25137]

def getScore(l, e):
    s = collections.deque()
    for x in l:
        i = c[x]
        if i // 4 == 0:
            s.append(i)
        else:
            if s[-1] == i % 4:
                s.pop()
            else:
                return p[i%4] if e else 0 
    if len(s) == 0:
        return 0
    score = 0
    while(s):
        score = score * 5 + s[-1] + 1
        s.pop()
    return 0 if e else score

with open("input") as f:
    error = 0
    scores = []
    for line in f:
        error += getScore(line[:-1], True)
        score = getScore(line[:-1], False)
        if score > 0:
            scores.append(score)
    print("Part one: ", error)
    print("Part two: ", sorted(scores)[len(scores)//2])