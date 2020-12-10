from pprint import pprint
import random

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

pprint(characterPercentages)

percentagesTab = []
for key, value in characterPercentages.items():
    percentagesTab.append((key, value))

percentagesTab.sort(key=lambda e: (e[1]))
pprint(percentagesTab)


percentagesTab1 = []
for key, value in occurenceTab.items():
    percentagesTab1.append((key, value))
percentagesTab1.sort(key=lambda e: (e[1]))

pprint(percentagesTab1)

    
def findClosest(character, occurenceTab, characterOccurences):
    close = []
    for letter in occurenceTab:
        distance = abs(occurenceTab[letter] - characterOccurences[character])
        if distance <= 0.4:
            close.append(letter.upper())
    return close

decoder = {}

for character in characterPercentages:
    closest = findClosest(character, occurenceTab, characterPercentages)
    decoder[character] = closest

word = "YFYŹYĄCSGCSG MOK QUTOŻCG"

for i in range(1000):
    newWord = ""
    for letter in word:
        if letter not in excluded:
            length = len(decoder[letter])
            if length == 0:
                newWord += "-"
            else:
                newWord += decoder[letter][int(random.randint(0, 1000))%length]
    print(newWord)
    