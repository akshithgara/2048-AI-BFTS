# Akshith Gara
# 2048 AI

from grid import grid
import random
class Node:
    def __init__(self, state, parent, action, pathCost):
        self.STATE = state  # The given 2048 initial state
        self.PARENT = parent  # A node instance, or none for the starting node
        self.ACTION = action  # A character, one of {LRUD}
        self.PATHCOST = pathCost  # Total number of moves

    def CHILDREN(self):
        childList = []
        curLayout = self.STATE
        curGrid = grid(current_grid=curLayout)
        directionList=['Left', 'Right', 'Up','Down']
        direction = random.choice(directionList)
        if grid.move(curGrid, direction):
            # Generate the state for the child
            childState = []
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, direction, self.PATHCOST + 1)
            childList.append(child)

        return childList
