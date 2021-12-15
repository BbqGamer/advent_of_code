from collections import defaultdict

def h(p):
    return (x_dest - p[0]) + (y_dest - p[1])

with open("input") as f:
    c = f.read().split("\n")[:-1]
    x_len = len(c)
    y_len = len(c[0])

    cave = {(x_len*i + x, y_len*j + y): (int(c[x][y])+i+j-1)%9+1 for i in range(5) for j in range(5) for x in range(x_len) for y in range(y_len)}
    
    x_dest = x_len * 5 - 1
    y_dest = y_len * 5 - 1

    dists = defaultdict(lambda a: float('inf'))
    best = float('inf')

    solver = []
    solver.append({'p': (0,0), "d" : 0})
    visited = set()

    while(solver):
        solver = list(filter(lambda a: a['p'] not in visited and a['d'] + h(a['p']) <= best, solver))
        min_i = None
        min_v = float('inf')
        for p in range(len(solver)):
            if solver[p]['d'] < min_v:
                min_v = solver[p]['d']
                min_i = p
        if min_i == None:
            continue
        p = solver.pop(min_i)
        visited.add(p['p'])
        x, y = p['p']
        N = filter(lambda a: a in cave, [(x+1,y),(x,y+1),(x-1,y),(x,y-1)])
        for n in N:
            dist = p['d'] + cave[n]
            if dist + h(n) >= best:
                continue
            if n == (x_dest, y_dest):
                best = min(dist, best)
                continue
            solver.append({'p': n, 'd':dist})
    print(best)