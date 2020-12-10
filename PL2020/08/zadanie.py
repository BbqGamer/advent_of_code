from pprint import pprint

import plot

characters = {}
characterCount = 0

occurenceTab = {"a": 	8.91, 	  "w": 	4.65, 	  "p": 	3.13, 	  "g": 	1.42, 	  "ć": 	0.40,
"i": 	8.21, 	  "s": 	4.32, 	  "m": 	2.80, 	  "ę": 	1.11, 	  "f": 	0.30,
"o": 	7.75, 	  "t": 	3.98, 	  "u": 	2.50, 	  "h": 	1.08, 	  "ń": 	0.20,
"e": 	7.66, 	  "c": 	3.96, 	  "j": 	2.28, 	  "ą": 	0.99, 	  "q": 	0.14,
"z": 	5.64, 	  "y": 	3.76, 	  "l": 	2.10, 	  "ó": 	0.85, 	  "ź": 	0.06,
"n": 	5.52, 	  "k": 	3.51, 	  "ł": 	1.82, 	  "ż": 	0.83, 	  "v": 	0.04,
"r": 	4.69, 	  "d": 	3.25, 	  "b": 	1.47, 	  "ś": 	0.66, 	  "x": 	0.02}

excluded = ['\n', ' ', '!', '"', ')', '*', '(', ',', '-',
             '.', ':', ';', '?', '[', ']', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open("input.txt", encoding="UTF-8") as f:
    for line in f:
        for character in line:
            if character in excluded:
                continue
            if not character in characters.keys():
                characters[character] = 1
            else:
                characters[character] += 1
            characterCount += 1

characterPercentages = {}

for character in characters:
    characterPercentages[character] = characters[character]/characterCount * 100


percentagesTab = []
for key, value in characterPercentages.items():
    percentagesTab.append((key, value))
percentagesTab.sort(key=lambda e: (e[1]))
#plot.drawTupleList(percentagesTab)


percentagesTab1 = []
for key, value in occurenceTab.items():
    percentagesTab1.append((key.upper(), value))
percentagesTab1.sort(key=lambda e: (e[1]))
#plot.drawTupleList(percentagesTab1)


def findClosest(character, occurenceTab, characterOccurences):
    minimumDist = 100
    for letter in occurenceTab:
        distance = abs(occurenceTab[letter] - characterOccurences[character])
        if distance < minimumDist:
            minimumDist = distance
            minimumChar = letter.upper()
    return minimumChar

decoder = {}

for character in characterPercentages:
    closest = findClosest(character, occurenceTab, characterPercentages)
    decoder[character] = closest


decoder['A'] = 'Ę' #OK
decoder['B'] = 'M'

decoder['Ć'] = 'Ż'




decoder['S'] = 'I' #OK
decoder['O'] = 'A' #OK
decoder['Y'] = 'O'
decoder['G'] = 'E'
decoder['Ę'] = 'G' #nie wiadomo
decoder['Q'] = 'W'
decoder['Ź'] = 'S'
decoder['L'] = 'T'
decoder['Ń'] = 'K'
decoder['I'] = 'C' #OK
decoder['Ó'] = 'H' #OK
decoder['R'] = 'Ł' #OK
decoder['Ś'] = 'Ą' #OK
decoder['K'] = 'Ś' #OK
decoder['W'] = 'L' #OK
decoder['Ł'] = 'P' #OK
decoder['Z'] = 'U' #OK
decoder['J'] = 'Ć' #OK
decoder['T'] = 'R' #OK
decoder['U'] = 'Y' 
decoder['P'] = 'Ó'
decoder['F'] = 'D'
decoder['Ż'] = 'Ź'
decoder['H'] = 'F'
decoder['N'] = 'Ń'

for key, value in decoder.items():
    if(value == 'A'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'C'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'F'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'G'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'J'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'L'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'O'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'U'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'W'):
        print(key, value)
print()

for key, value in decoder.items():
    if(value == 'Z'):
        print(key, value)
print()

text = []

with open("input.txt") as f:
    for line in f:
        for character in line:
            if character in excluded:
                text.append(character)
            else:
                text.append(decoder[character])


def convert(s): 
    new = "" 
    for x in s: 
        new += x  
    return new 

sum = 0
valuesToSum = ['A', 'C', 'F', 'G', 'J', 'L', 'O', 'U', 'W', 'Z']
for char in convert(text):
    if char in valuesToSum:
        sum += 1

print(sum)

sum = 0

strtext = convert(text)


"""
text_file = open("output.txt", "w")
n = text_file.write(convert(text))
text_file.close()
"""