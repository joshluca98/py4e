
wordDictionary = dict() # create empty dictionary

count = 0 # start the counter at 0

file = open("words.txt") # open the words.txt file

for line in file: # read each line in the file one by one
    words = line.split() # split each line into a list of words
    for word in words: # read each word in the words list
        count += 1 # add 1 to the counter for every word in the list
        if word in wordDictionary: # if the word is already in the dictionary..
            continue # then we go to the top of the loop (word is skipped)
        wordDictionary[word] = count # if word is not in list already, it is added to the dictionary with a value of the counter variable

# search for a word to see if it is found as a key in the dictionary
while True:
    wordSearch = input("Enter a word to check if in the dictionary: ")
    if wordSearch == "STOP": # if "STOP" is entered the loop terminates
        break
    if wordSearch in wordDictionary:
        print("'" + wordSearch + "'" + " is in the dictionary")
    else:
        print("'" + wordSearch + "'" + " is NOT in the dictionary")
        