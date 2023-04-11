import re

fileName = "mbox-short.txt"
file = open(fileName)

regex = input("Enter a regular expression: ")
counter = 0

for line in file:
    line = line.rstrip()
    x = re.findall(regex, line)
    if len(x) > 0:
        counter += 1

print("The file had " + str(counter) + " lines that matched " + "'" + regex + "'")