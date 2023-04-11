
wordDictionary = dict() # create empty dictionary

fileName = input("Enter file name: ") # ask for file name

file = open(fileName) # open the file using file name provided

for line in file: # read each line in the file one by one
    if line != '\n': # only process lines that are not empty
        words = line.split() # split lines into list of words
        if words[0] == "From": # only process lists that begin with the word "From"
            for word in words: # read each word one by one
                index = word.find('@') # search for @ symbol in the word
                if index != -1: # if the @ is located
                    domain = word[index+1:] # parse the domain from the whole email "word"
                    if domain not in wordDictionary: # if the domain isn't in the dictionary then add it
                        wordDictionary[word[index+1:]] = 1
                    else: # if it is in the dictionary, then add 1 to its value
                        wordDictionary[word[index+1:]] += 1

print(wordDictionary) # print the entire dictionary
    
        