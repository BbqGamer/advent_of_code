def addPoint(x,y, points):
    point = f"{x},{y}"
    if point not in points:
        points[point] = 0
    points[point] += 1

def drawHorizontal(x0, y0, x1, y1):
    for i in range(min(x0,x1), max(x0,x1)+1):
        addPoint(i, y0, points1)
        addPoint(i, y0, points2)

def drawVertical(x0, y0, x1, y1):
    for i in range(min(y0, y1), max(y0, y1)+1):
        addPoint(x0, i, points1)
        addPoint(x0, i, points2)

def drawDiagonal(x0, y0, x1, y1):
    xc = 1 if x1 > x0 else -1
    yc = 1 if y1 > y0 else -1
    while(x0 != x1):
        addPoint(x0, y0, points2)
        x0 += xc
        y0 += yc
    addPoint(x0, y0, points2)    

with open("input") as f:
    points1 = {}
    points2 = {}
    for line in f:
        p0, p1 = [[int(x) for x in p.split(",")] for p in line.split(" -> ")]
        x0, y0 = p0
        x1, y1 = p1
        if y1 == y0:
            drawHorizontal(x0, y0, x1, y1)
        elif x0 == x1:
            drawVertical(x0, y0, x1, y1)
        else:
            drawDiagonal(x0, y0, x1, y1)
    counter1 = len([1 for v in points1.values() if v > 1])
    counter2 = len([1 for v in points2.values() if v > 1])
    print("Part 1: ", counter1)
    print("Part 2: ", counter2)