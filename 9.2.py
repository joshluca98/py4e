
wordDictionary = dict() # create empty dictionary

fileName = input("Enter file name: ")
file = open(fileName) # open the file

for line in file: # read each line in the file one by one
    if line != '\n':
        words = line.split()
        if words[0] == "From":
            wordDictionary[words[2]] = wordDictionary.get(words[2], 0) + 1
            
print(wordDictionary)
    
        