from collections import namedtuple

with open('input.txt', 'r') as f:
    instructions = list(map(lambda x : (x[0],int(x[1:])), f.read().split(',')))

ups = 0
downs = 0
rights = 0
lefts = 0
for i in instructions:
    if i[0] == "U":
        ups += i[1]
    elif i[0] == "D":
        downs += i[1]
    elif i[0] == "L":
        lefts += i[1]
    else:
        rights += i[1]


tab = [[0 for i in range(ups+downs+1)]for i in range(rights+lefts+1)]



