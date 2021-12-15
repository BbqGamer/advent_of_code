from heapq import heapify, heappush, heappop

with open("input") as f:
    c = f.read().split("\n")[:-1]
    x_len = len(c)
    y_len = len(c[0])

    cave = {(x_len*i + x, y_len*j + y): (int(c[x][y])+i+j-1)%9+1 for i in range(5) for j in range(5) for x in range(x_len) for y in range(y_len)}
    
    x_dest = x_len * 5 - 1
    y_dest = y_len * 5 - 1

    best = float('inf')

    solver = []
    heapify(solver)
    heappush(solver, (0, (0,0)))

    visited = set()

    def h(p):
        return (x_dest - p[0]) + (y_dest - p[1])

    while(solver):
        p = heappop(solver)
        if p == None:
            break
        if p[0] >= best:
            break
        x, y = p[1]
        N = filter(lambda a: a in cave, [(x+1,y),(x,y+1),(x-1,y),(x,y-1)])
        for n in N:
            dist = p[0] + cave[n]
            if dist + h(n) >= best:
                continue
            if n == (x_dest, y_dest):
                best = min(dist, best)
                continue
            if n not in visited:
                heappush(solver, (dist,n))
                visited.add(n)
    print(best)