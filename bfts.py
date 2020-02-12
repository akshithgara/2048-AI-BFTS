from node import Node
from grid import grid

def isGoal(state):
#     currState = state.get_current_grid()
    win = 8
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


def BFTS(state):
    frontier = []
    root = Node(state, None, None, 0)
    frontier.append(root)
    visited = []
    count = 0

    while len(frontier) != 0:
        curNode = frontier.pop(0)
        visited.append(curNode)

#         print(curNode.ACTION)
#         print(curNode.STATE)
        if isGoal(curNode.STATE):
            sequence = []
            curTracing = curNode

            while curTracing.PARENT != None:
                sequence.append(curTracing.ACTION)

#                 print(curTracing.PARENT.STATE)
                curTracing = curTracing.PARENT
            sequence.reverse()
            return sequence, curNode

        for child in curNode.CHILDREN():
            if child not in visited:
                frontier.append(child)
