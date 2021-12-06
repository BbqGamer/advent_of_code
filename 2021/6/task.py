with open("input") as f:
    inputFish = [int(x) for x in f.readline().rstrip().split(",")]
    fish = [inputFish.count(i) for i in range(9)]
    zeros = 0
    for i in range(256):
        newFish = [0 for i in range(9)]
        zeros = fish[0]
        newFish[0] = 0
        for k in range(1,9):
                newFish[k-1] = fish[k]
        newFish[6] += zeros
        newFish[8] += zeros
        fish = newFish
        if i == 79:
            print("Part 1: ", sum(fish))    
    print("Part 2: ", sum(fish))