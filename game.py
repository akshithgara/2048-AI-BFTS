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
    startTime = datetime.now()
    # Solution goes here


    sol = BFTS(firstState, goal, spawnList)
    print(sol[0])
    print(sol[1].STATE)
    endTime = datetime.now()
