import numpy as np
from copy import deepcopy

#TASK 1
with open("input") as f:
    message = np.array([[int(x) for x in line[:-1]] for line in f])
    counts = np.count_nonzero(message, axis=0)
    l = message.shape[0]
    gamma = counts > l - counts
    gamma = int("".join(str(int(x)) for x in list(gamma)), 2)
    mask = 2 ** message.shape[1] - 1
    epsilon = gamma ^ mask
    print("Part one:", gamma * epsilon)            
    
#TASK 2
with open("input") as f:
    oxygen = [[int(x) for x in line[:-1]] for line in f]
    CO2 = deepcopy(oxygen)
    i = 0
    while(len(oxygen) > 1):
        ones = [oxygen[x][i] for x in range(len(oxygen))].count(1)
        mostCommon = 1 if ones >= len(oxygen) - ones else 0
        oxygen = list(filter(lambda a: a[i] == mostCommon, oxygen))
        i += 1

    i = 0
    while(len(CO2) > 1):
        zeros = [CO2[x][i] for x in range(len(CO2))].count(0)
        leastCommon = 0 if zeros <= len(CO2) - zeros else 1
        CO2 = list(filter(lambda a: a[i] == leastCommon, CO2))
        i += 1
    
    oxygen = int("".join(str(int(x)) for x in oxygen[0]), 2)
    CO2 = int("".join(str(int(x)) for x in CO2[0]), 2)
    print("Part two:", oxygen * CO2)    
