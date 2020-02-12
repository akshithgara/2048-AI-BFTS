import queue
from node import Node
from grid import grid

def isGoal(state):
    # currState = state.get_current_grid()
    win = 8
    for line in state:
        for i in line:
            if i == win:
                return True
    return False


def BFTS(state):
    frontier = queue.Queue()
    root = Node(state, None, None, 0)
    frontier.put(root)


    while True:
        if frontier.empty():
            return None

        curNode = frontier.get()
        # print(curNode.STATE)
        if isGoal(curNode.STATE):
            sequence = []
            curTracing = curNode

            while curTracing.PARENT is not None:
                sequence.append(curTracing.ACTION)
                curTracing = curTracing.PARENT
                print(sequence)
            sequence.reverse()
            return (sequence, curNode)

        for child in curNode.CHILDREN():
            print('hits')
            frontier.put(child)
