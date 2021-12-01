with open("input") as f:
    data = [int(line) for line in f]
    grouped = [sum(data[x:x+3]) for x in range(len(data)-2)]
    print("Part 1: ", sum([1 if data[x] > data[x-1] else 0 for x in range(1, len(data))]))
    print("Part 2: ", sum([1 if grouped[x] > grouped[x-1] else 0 for x in range(1, len(grouped))]))