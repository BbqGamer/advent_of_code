with open("input") as f:
    count = 0
    for line in f:
        inp, out = line.split("|")
        for digit in out.split():
            if len(digit.strip()) in [2, 4, 3, 7]:
                count += 1
    print(count)