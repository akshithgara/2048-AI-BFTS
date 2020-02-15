# Akshith Gara
# 2048 AI
# CS5400

from node import Node


# Function to check if the goal state has been achieved.
def isGoal(state, goal):
    win = goal
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


# Breadth First Tree Search function to traverse through the given input and the give the shortest route.
def BFTS(state, goal, spawnList):
    frontier = []
    root = Node(state, None, None, 0, 0)
    frontier.append(root)

    while len(frontier) != 0:
        curNode = frontier.pop(0)

        if isGoal(curNode.STATE, goal):

            sequence = []
            curTracing = curNode
            while curTracing.PARENT is not None:
                sequence.append(curTracing.ACTION)
                curTracing = curTracing.PARENT
            sequence.reverse()

            return sequence, curNode

        for child in curNode.CHILDREN(spawnList):
            frontier.append(child)
