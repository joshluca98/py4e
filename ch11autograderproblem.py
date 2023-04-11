import re

file = open("regex_sum_1620464.txt")

total = 0

for line in file:
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        total += sum(map(int, x))

print(total)