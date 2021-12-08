letters = ["a","b","c","d","e","f","g"] 
knownLengths = {2: 1, 3: 7, 4: 4, 7: 8}

with open("input") as f:
    result = 0
    for line in f:
        inp, out = [list(map(set, x.strip().split())) for x in line.split("|")]
        assignments = {i:set() for i in range(10)}
        letterA = {i: None for i in letters}
        for i in inp:
            l = len(i)
            if l in knownLengths.keys():
                assignments[knownLengths[l]] = i
        #get 3, 2 and 5
        for i in [x for x in inp if len(x) == 5]:
            if len(i - assignments[1]) == 3:
                assignments[3] = i
            elif len(i - assignments[4]) == 3:
                assignments[2] = i
            elif len(i - assignments[4]) == 2:
                assignments[5] = i

        #get 0, 6 and 9
        for i in [x for x in inp if len(x) == 6]:
            if len(i - assignments[1]) == 5:
                assignments[6] = i
            elif len(i - assignments[4]) == 3:
                assignments[0] = i
            else:
                assignments[9] = i
                
        num = ""
        for o in out:
            for k, v in assignments.items():
                if v == o:
                    num += str(k)     
        
        result += int(num)
print(result)