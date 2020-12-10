adapters = []
with open("input.txt") as f:
    for number in f:
        adapters.append(int(number))

adapters.sort()
adapters.insert(0, 0)
adapters.insert(len(adapters), adapters[-1] + 3)

def getNearbyNodes(adapterIndex, adapters):
    tab = []
    for candidateIndex in range(adapterIndex + 1, len(adapters)):
        if(adapters[candidateIndex] - adapters[adapterIndex] in (1,2,3)):
            tab.append(candidateIndex)
    return tab

def createGraph(adapters):
    graph = {}
    for adapterIndex, adapter in enumerate(adapters):
        graph[adapterIndex] = getNearbyNodes(adapterIndex, adapters)
    return graph

graph = createGraph(adapters)

resultTab = [None for x in graph.keys()]

def countPaths(startingI, endingI, adapters, graph):
    if resultTab[startingI] != None:
        return resultTab[startingI]
    if startingI == endingI:
        return 1
    else:
        count = 0
        for end in graph[startingI]:
            count += countPaths(end, endingI, adapters, graph)
        resultTab[startingI] = count
        return count

print(countPaths(0, 113, adapters, graph))