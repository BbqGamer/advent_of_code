from pprint import pprint

rules = {}

with open("input.txt") as f:
    for line in f:
        rightTab = []

        splitted = line.split(" bags contain ")
        left = splitted[0]
        right = splitted[1]

        for rightItem in right.split(", "):
            itemSplitted = rightItem.split(" ")
            quantity = itemSplitted[0]
            if quantity == 'no':
                itemRecord = None
                rightTab.append(itemRecord)
                break
            else:
                quantity = int(quantity)

            itemRecord = (quantity, itemSplitted[1] + " " + itemSplitted[2])
            rightTab.append(itemRecord)
        
        rules[left] = rightTab

count = 0

def countBags(rules, rule):
    if rules[rule] == [None]:
        return 0

    count = 0
    
    for item in rules[rule]:
        count += item[0]
        for i in range(item[0]):
            count += countBags(rules, item[1])
    
    return count

print(countBags(rules, "shiny gold"))


