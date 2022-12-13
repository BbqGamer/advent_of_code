def compare_lists(left, right) -> int:
    i = 0
    while(True):
        if i == len(left) and i == len(right):
            return 0
        elif i == len(left):
            return -1
        elif i == len(right):
            return 1

        if(type(left[i]) == list and type(right[i]) == list):
            res = compare_lists(left[i], right[i])
            if res != 0: return res
        elif(type(left[i]) == list):
            res = compare_lists(left[i], [right[i]])
            if res != 0: return res
        elif(type(right[i]) == list):
            res = compare_lists([left[i]], right[i])
            if res != 0: return res
        else:
            if left[i] < right[i]:
                return -1
            if left[i] > right[i]:
                return 1
        i += 1


with open("input/data", "r") as f:
    suma = 0
    packets = []
    for index, test in enumerate(f.read().split("\n\n")):
        a, b = test.split("\n")
        a = eval(a)
        b = eval(b)
        packets.append(a)
        packets.append(b)
        
        res = compare_lists(a,b)
        if res == -1:
            suma += index + 1
    print("Part2: ", suma)

    #sort packets
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if compare_lists(packets[j], packets[j+1]) == 1:
                tmp = packets[j].copy()
                packets[j] = packets[j+1].copy()
                packets[j+1] = tmp.copy()

    p1 = [[2]]
    for i in range(len(packets)):
        if(compare_lists(p1, packets[i]) == -1):
            pos1 = i + 1
            break

    p1 = [[6]]
    for j in range(len(packets)):
        if(compare_lists(p1, packets[j]) == -1):
            pos2 = j + 2
            break   

    print("Part 2: ", pos1 * pos2)

