# Akshith Gara
# 2048 AI


def validMove(y, x, layout):
    if x < 0 or y < 0:
        return False
    if y >= len(layout) or x >= len(layout[0]):
        return False
    return True

#To be continued