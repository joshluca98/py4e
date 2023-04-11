romeoFile = open('romeo.txt')
romeoText = romeoFile.read()
romeoText = romeoText.split()

uniqueWords = []

for word in romeoText:
    if word not in uniqueWords:
        uniqueWords.append(word)

uniqueWords.sort()
print(uniqueWords)