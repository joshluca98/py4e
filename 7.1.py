# Open the file
fileName = input("Enter a file name: ")
textFile = open(fileName)
# Loop through all the lines and print them out in all upper case
for line in textFile:
    line = line.upper()
    print(line)