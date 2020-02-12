# Akshith Gara
# 2048 AI

from grid import grid

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
        if grid.move(curGrid, 'Left'):
            # Generate the state for the child
            childState = []
            print("tries l")
            print(curGrid.get_current_grid())
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'Left', self.PATHCOST + 1)
            childList.append(child)
        if grid.move(curGrid, 'Right'):
            childState = []
            print("tries r")
            print(curGrid.get_current_grid())
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'Right', self.PATHCOST + 1)
            childList.append(child)
        if grid.move(curGrid, 'Up'):
            childState = []
            print("tries u")
            print(curGrid.get_current_grid())
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'Up', self.PATHCOST + 1)
            childList.append(child)
        if grid.move(curGrid, 'Down'):
            childState = []
            print("tries d")
            print(curGrid.get_current_grid())
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'Down', self.PATHCOST + 1)
            childList.append(child)
        return childList
