with open("input") as f:
    inputFish = [int(x) for x in f.readline().rstrip().split(",")]
    fish = {i:inputFish.count(i) for i in range(9)}
    zeros = 0
    for i in range(256):
        newFish = {i:0 for i in range(9)}
        for k in range(9):
            if k == 0:
                zeros = fish[k]
                newFish[k] = 0
            else:
                newFish[k-1] = fish[k]
        newFish[6] += zeros
        newFish[8] += zeros
        fish = newFish
        if i == 79:
            print("Part 1: ", sum(fish.values()))    
    print("Part 2: ", sum(fish.values()))