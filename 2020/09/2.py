numbers = []

def isValid(number):
    for letter in lastLetters:
        if(number - letter) in lastLetters:
            return True
    return False

with open("input.txt") as f:
    for line in f:
        numbers.append(int(line))


INVALID = 22406676


for startingIndex in range(len(numbers)):
    sumOfnumbers = numbers[startingIndex]
    for endingIndex in range(startingIndex + 1, len(numbers)):
        sumOfnumbers += numbers[endingIndex]
        if(sumOfnumbers == INVALID):
            print(numbers[startingIndex] + numbers[endingIndex])
            break
        if(sumOfnumbers > INVALID):
            break


smallest = 1000000
biggest = 0

for i in range(393, 410):
    if(numbers[i] > biggest):
        biggest = numbers[i]
    if(numbers[i] < smallest):
        smallest = numbers[i]

print()
print(smallest + biggest)
print()
print(smallest)
print(biggest)




    

