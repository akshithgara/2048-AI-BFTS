from node import Node
from grid import grid

def isGoal(state):
    win = 16
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


def BFTS(state):
    frontier = []
    root = Node(state, None, None, 0, 0)
    frontier.append(root)

    while len(frontier) != 0:
        curNode = frontier.pop(0)

        if isGoal(curNode.STATE):

            sequence = []
            curTracing = curNode
            while curTracing.PARENT != None:
                sequence.append(curTracing.ACTION)
                curTracing = curTracing.PARENT
                print("Parent:", curTracing.STATE)
            sequence.reverse()

            return sequence, curNode

#         print("parent node:", curNode.STATE)
        for child in curNode.CHILDREN():
#             print("child nodes: ", child.STATE)
            frontier.append(child)


