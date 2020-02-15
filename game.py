# Akshith Gara
# 2048 AI
# CS5400

import sys
from datetime import datetime
from bfts import BFTS

from scraper import *

if __name__ == '__main__':

    if len(sys.argv) > 1:
        inputFile = sys.argv[1]
    else:
        inputFile = input("Please enter the filename: ")

    firstState, goal, spawnList = inputGrabber(inputFile)
    # Timer to measure the execution time.
    startTime = datetime.now()
    sol = BFTS(firstState, goal, spawnList)
    endTime = datetime.now()
    execTime = endTime - startTime
    print(execTime.microseconds)
    print(sol[1].PATHCOST)
    print(''.join(sol[0]))
    for line in sol[1].STATE:
        print(' '.join([str(x) for x in line]))
