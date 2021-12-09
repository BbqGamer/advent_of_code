with open("input") as f:
    matrix = [[int(x) for x in line[:-1]] for line in f]
    risks = 0
    
    def getNeighbours(i, j):
        neigbours = []
        for x, y in [(-1,0), (1, 0), (0, 1), (0, -1)]:
            if i + x < 0 or j + y < 0:
                continue
            try:
                neigbours.append(matrix[i+x][j+y])
            except:
                pass
        return neigbours

    def getRisk(i, j):
        risk = 0
        if all([x > matrix[i][j] for x in getNeighbours(i,j)]):
            risk = matrix[i][j] + 1
        return risk

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            risks += getRisk(i,j)
    print(risks)