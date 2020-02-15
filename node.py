# Akshith Gara
# 2048 AI
# CS5400

from grid import grid


class Node:
    def __init__(self, state, parent, action, pathCost, spawn):
        self.STATE = state  # The given 2048 initial state.
        self.PARENT = parent  # A node instance, or none for the starting node.
        self.ACTION = action  # A character, one of {LRUD}.
        self.PATHCOST = pathCost  # Total number of moves.
        self.SPAWN = spawn # Stores the current spawn value from the given list.

    def CHILDREN(self, sl): # Function to try out all the moves and add it to the childList.
        childList = []
        curLayout = self.STATE
        curGrid = grid(current_grid=curLayout, spawn_list=sl)
        currState = self
        if grid.move(curGrid, 'Up', self.SPAWN):
            # Generate the state for the child
            childState = []
            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'U', self.PATHCOST + 1, self.SPAWN + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout, spawn_list=sl)

        if grid.move(curGrid, 'Down', self.SPAWN):
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'D', self.PATHCOST + 1, self.SPAWN + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout, spawn_list=sl)

        if grid.move(curGrid, 'Left', self.SPAWN):
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'L', self.PATHCOST + 1, self.SPAWN + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout, spawn_list=sl)

        if grid.move(curGrid, 'Right', self.SPAWN):
            childState = []

            for line in curGrid.get_current_grid():
                childState.append(line)
            child = Node(childState, self, 'R', self.PATHCOST + 1, self.SPAWN + 1)
            childList.append(child)
            curLayout = self.STATE
            curGrid = grid(current_grid=curLayout, spawn_list=sl)

        return childList
