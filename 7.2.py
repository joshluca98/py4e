# Prompt for file name
fileName = input("Enter a file name: ")
# Open the file
textFile = open(fileName)
# Loop through all the lines

counter = 0
totalFloatValue = 0.0

for line in textFile:
    # search for specific starting phrase
    if line.startswith('X-DSPAM-Confidence:'):
        # count number of times found
        counter = counter + 1
        # look for colon
        pos = line.find(':')
        # parse float value that comes after the colon
        extractedNumber = float(line[pos + 1 : ])
        # add parsed float value to the total float value
        totalFloatValue = totalFloatValue + extractedNumber
   
# compute average of float values and print it
averageValue = totalFloatValue / counter
print("Average spam confidence:", averageValue)
