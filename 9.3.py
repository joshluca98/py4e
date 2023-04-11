
wordDictionary = dict() # create empty dictionary

fileName = input("Enter file name: ")
file = open(fileName) # open the file

for line in file: # read each line in the file one by one
    if line != '\n':
        words = line.split()
        if words[0] == "From":
            wordDictionary[words[1]] = wordDictionary.get(words[1], 0) + 1
            
print(wordDictionary)
    
        