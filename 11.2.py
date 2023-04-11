import re

fileName = "mbox-short.txt"
file = open(fileName)

total = 0
divisor = 0

for line in file:
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        total = total + int(x[0])
        divisor = divisor + 1

print(int(total / divisor))