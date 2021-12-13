import matplotlib.pyplot as plt

with open("input") as f:
    d, f = f.read().split("\n\n")
    dots = set([tuple(map(int, dot.split(","))) for dot in d.split("\n")])
    f = [[fold.split("=")[0][-1], int(fold.split("=")[1])] for fold in f.split("\n")]
    
    for i in range(len(f)):
        n = set()
        for d in dots:
            axis = f[i][0]
            fold = f[i][1]
            x, y = d[0], d[1]
            if axis == "x":
                if x > fold:
                    x = fold - (x - fold)
            else:
                if y > fold:
                    y = fold - (y - fold)
            n.add((x, y))
        dots = n
        if i == 0:
            print(len(dots))
    X = []
    Y = []
    for d in dots:
        X.append(d[0])
        Y.append(-d[1])
    plt.scatter(X,Y)
    plt.show()