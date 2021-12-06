def cross(b, n):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == n:
                b[i][j] = int(b[i][j])

def check(b):
    if any([all([1 if type(i[x]) is int else 0 for x in range(len(b[0]))]) for i in b]):
        return True
    if any([all([1 if type(b[i][x]) is int else 0 for i in range(len(b))]) for x in range(len(b))]):
        return True
    return False

def getUnmarked(b):
    return sum([sum([int(j) for j in i if type(j) == str]) for i in b])

with open("input") as f:
    data = f.read()[:-2]
    shots = [x for x in data.split("\n")[0].split(",")]
    boards = [[[j for j in i.split()] for i in b.split("\n")] for b in data.split("\n\n")[1:]]
    #FIRST PART
    finished = False
    for i in shots:
        if finished:
            break
        for b in boards:
            cross(b, i)
            if check(b):
                unmarked = getUnmarked(b)
                print(unmarked * int(i))
                finished = True
    
    #SECOND PART
    won = set()
    for i in shots:
        for b in range(len(boards)):
            if b in won:
                continue
            cross(boards[b], i)
            if check(boards[b]):
                won.add(b)
                lastWon = (boards[b], i)
    unmarked = getUnmarked(lastWon[0])
    print(unmarked * int(lastWon[1]))
                

