# Akshith Gara
# 2048 AI
# CS5400

import sys
import bfts
from datetime import datetime

# Takes in input from the file passed as argument
if len(sys.argv) > 1:
    inputFile = sys.argv[1]
else:
    inputFile = input("Please enter the filename: ")


# Reads each line from the file and stores each line in one element of a list
grabbed = False
while not grabbed:
    try:
        with open(inputFile) as file:
            scrapedLines = list(file)
            grabbed = True
    except Exception as e:
        print("Error!")
        inputFile = input("Please enter another file name: ")

# Removes the trailing new line characters
for line in range(len(scrapedLines)):
    scrapedLines[line] = scrapedLines[line].replace('\n', '')

# Stores goal and spawn numbers
maxNum = scrapedLines[0]
spawnNums = list(scrapedLines[1].split(' '))

# test
print(maxNum)
print(spawnNums)

# extracts the first state from the given 2048 puzzle
firstState = scrapedLines
del firstState[0]
del firstState[0]

print(firstState)

startTime = datetime.now()
# Solution goes here
endTime = datetime.now()