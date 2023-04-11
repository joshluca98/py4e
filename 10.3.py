
import string

wordDictionary = dict() # create empty dictionary

#fileName = input("Enter file name: ")
fileName = "example.txt"
file = open(fileName) # open the file

for line in file:

    if line != '\n':
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            for char in word:
                wordDictionary[char] = wordDictionary.get(char, 0) + 1
            
lst = list()
for key, val in list(wordDictionary.items()):
    lst.append((val, key))
lst = sorted(lst, reverse=True)
for key, val in lst:
    print(key, val)      