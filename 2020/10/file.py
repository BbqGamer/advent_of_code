adapters = []

with open("input.txt") as f:
    for number in f:
        adapters.append(int(number))

adapters.sort()
adapters.insert(0, 0)

oneDifferences = 0
threeDifferences = 0

for i in range(1, len(adapters)):
    if(adapters[i] - adapters[i-1] == 1):
        oneDifferences += 1
    elif(adapters[i] - adapters[i-1] == 3):
        threeDifferences += 1
    print(str(adapters[i]) + " " + str(adapters[i] - adapters[i-1]))


threeDifferences += 1

print(oneDifferences * threeDifferences)


