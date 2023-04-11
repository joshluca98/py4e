
wordDictionary = dict() # create empty dictionary

#fileName = input("Enter file name: ")
fileName = "mbox-short.txt"
file = open(fileName) # open the file

for line in file:
    if line != '\n':
        words = line.split()
        if words[0] == "From":
            time = words[5]
            wordDictionary[(time[:2])] = wordDictionary.get(time[:2], 0) + 1
            
lst = list()
for key, val in list(wordDictionary.items()):
    lst.append((key, val))
lst = sorted(lst)
for key, val in lst:
    print(key, val)      