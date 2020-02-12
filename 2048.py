# Akshith Gara
# 2048 AI
# CS5400

import sys
from grid import grid
from datetime import datetime
from bfts import BFTS


spCount = 0
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
for num in range(len(spawnNums)):
    spawnNums[num] = int(spawnNums[num])


# extracts the first state from the given 2048 puzzle and converts them to nested list of numbers
for line in range(2, len(scrapedLines)):
    scrapedLines[line] = list(scrapedLines[line].split(' '))

firstState = scrapedLines
del firstState[0]
del firstState[0]

for i in range(len(firstState)):
    for j in range(len(firstState[i])):
        firstState[i][j] = int(firstState[i][j])

# test
# print(maxNum)
# print(spawnNums)
# print(firstState)
# newGrid = grid(current_grid=firstState)
# grid.move(newGrid, 'Left')
# # grid.current_grid = newGrid
# print(newGrid.get_current_grid())




startTime = datetime.now()
# Solution goes here

sol = BFTS(firstState)

print(sol[0])
endTime = datetime.now()
