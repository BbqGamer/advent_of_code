countFlashes = 0

def getNeighbours(m, x, y):
    n = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                I = x + i
                J = y + j
                if I >= 0 and I < len(m) and J >= 0 and J < len(m[0]):
                    n.append((I,J))
    return n

def updateCell(m, i, j):
    global countFlashes
    m[i][j] += 1
    if m[i][j] == 10:
        countFlashes += 1
        for x, y in getNeighbours(m, i, j):
            updateCell(m, x, y)
    elif m[i][j] > 10:
        return

def updateBoard(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            updateCell(m, i, j)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] >= 10:
                m[i][j] = 0
    
with open("input") as f:
    m = [list(map(int,line.rstrip())) for line in f]
    size = len(m) * len(m[0])
    part1 = part2 = i = 0
    while(not part1 or not part2):
        i += 1
        flashesBefore = countFlashes
        updateBoard(m)
        if not part2 and countFlashes - flashesBefore == size:
            print("Part two: ", i)
            part2 = 1
        if not part1 and i == 100:
            print("Part one: ", countFlashes)
            part1 = 1