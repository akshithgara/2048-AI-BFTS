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
        currState = self
        if grid.move(curGrid, 'Up'):
            # Generate the state for the child
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'U', self.PATHCOST + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout)

        if grid.move(curGrid, 'Down'):
            childState = []


            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'D', self.PATHCOST + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout)

        if grid.move(curGrid, 'Left'):
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'L', self.PATHCOST + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout)

        if grid.move(curGrid, 'Right'):
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'R', self.PATHCOST + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout)


        return childList
