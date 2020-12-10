tab = []

with open("input.txt") as f:
    for line in f:
        t = int(line.split(" ")[0])
        w = int(line.split(" ")[1])
        tab.append((t, w))

def getPrice(tab):
    price = 0
    time = 0
    for i in tab:
        time += i[0]
        price += i[1] * time
    return price

#times
tab1 = tab
tab1.sort(key=lambda e: (e[0]))
print(getPrice(tab1))
print()

#priorities
tab1 = tab
tab1.sort(key=lambda e: (e[1]))
print(getPrice(tab1))
print()

#times and priorities
tab1 = tab
tab1.sort(key=lambda e: (e[0], e[1]))
print(getPrice(tab1))
print()

#priorities and times
tab1 = tab
tab1.sort(key=lambda e: (e[1], e[0]))
print(getPrice(tab1))
print()

#priorities * times
tab1 = tab
tab1.sort(key=lambda e: (e[1] * e[0]))
print(getPrice(tab1))
print()

#priorities / times
tab1 = tab
tab1.sort(key=lambda e: (e[1] / e[0]))
print(getPrice(tab1))
print()

#times / priorities
tab1 = tab
tab1.sort(key=lambda e: (e[0] / e[1]))
print(getPrice(tab1))
print()

#priorities * times revert
tab1 = tab
tab1.sort(key=lambda e: (e[1] * e[0]))
tab1.reverse()
print(getPrice(tab1))
print()

#priorities revert
tab1 = tab
tab1.sort(key=lambda e: (e[1]))
tab1.reverse()
print(getPrice(tab1))
print()

#times and priorities revert
tab1 = tab
tab1.sort(key=lambda e: (e[0], e[1]))
tab1.reverse()
print(getPrice(tab1))
print()

#priorities and times revert
tab1 = tab
tab1.sort(key=lambda e: (e[1], e[0]))
tab1.reverse()
print(getPrice(tab1))
print()

#priorities * times revert
tab1 = tab
tab1.sort(key=lambda e: (e[1] * e[0]))
tab1.reverse()
print(getPrice(tab1))
print()

#priorities / times revert 
tab1 = tab
tab1.sort(key=lambda e: (e[1] / e[0]))
tab1.reverse()
print(getPrice(tab1))
print()

#times / priorities revert
tab1 = tab
tab1.sort(key=lambda e: (e[0] / e[1]))
tab1.reverse()
print(getPrice(tab1))
print()

