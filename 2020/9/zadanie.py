lastLetters = []

def isValid(number):
    for letter in lastLetters:
        if(number - letter) in lastLetters:
            return True
    return False

with open("input.txt") as f:
    for i in range(25):
        lastLetters.append(int(f.readline()))
    for line in f:
        newNumber = int(line)

        if(not isValid(newNumber)):
            print(line)
            break

        lastLetters.pop(0)
        lastLetters.append(newNumber)

