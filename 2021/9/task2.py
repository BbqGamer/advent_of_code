with open("input") as f:
    matrix = [[int(x) for x in line[:-1]] for line in f]
    risks = 0
    
    def getNeighbours(i, j):
        neigbours = []
        for x, y in [(-1,0), (1, 0), (0, 1), (0, -1)]:
            if i + x >= 0 and j + y >= 0 and i + x < len(matrix) and j + y < len(matrix[i]):
                neigbours.append((i+x,j+y))
        return neigbours

    def isMinima(i, j):
        return True if all([matrix[x][y] > matrix[i][j] for x,y in getNeighbours(i,j)]) else False
    
    def getMinimas():
        minimas = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if isMinima(i, j):
                    minimas.append((i,j))
        return minimas

    visited = set()

    def getBasin(i, j):
        size = 1
        visited.add((i,j))
        for x,y in getNeighbours(i, j):
            if (x,y) not in visited and matrix[x][y] > matrix[i][j] and matrix[x][y] != 9:
                size += getBasin(x, y)
        return size

    sizes = []
    for x,y in getMinimas():
        sizes.append(getBasin(x,y))
    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])