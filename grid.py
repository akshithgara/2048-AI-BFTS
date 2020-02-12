# Akshith Gara
# 2048 AI
# CS5400


# type object argument after * must be an iterable, not grid
def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]


def move_is_possible(direction, field1):
    def row_is_left_movable(row):
        def change(i):  # true if there'll be change in i-th tile
            if row[i] == 0 and row[i + 1] != 0:  # Move
                return True
            if row[i] != 0 and row[i + 1] == row[i]:  # Merge
                return True
            return False

        return any(change(i) for i in range(len(row) - 1))

    # //direction   0: up, 1: right, 2: down, 3: left
    check = {}
    check['Left'] = lambda field: \
        any(row_is_left_movable(row) for row in field)

    check['Right'] = lambda field: \
        check['Left'](invert(field))

    check['Up'] = lambda field: \
        check['Left'](transpose(field))

    check['Down'] = lambda field: \
        check['Right'](transpose(field))

    if direction in check:
        # //direction   0: up, 1: right, 2: down, 3: left
        return check[direction](field1)
    else:
        return False



def spawn(field, spawnNums, spawnCount):
    new_element = spawnNums[spawnCount]
    if field[0][0] == 0:
        field[0][0] = new_element
    elif field[0][len(field) - 1] == 0:
        field[0][len(field) - 1] = new_element
    elif field[len(field) - 1][len(field) - 1] == 0:
        field[len(field) - 1][len(field) - 1] = new_element
    elif field[len(field) - 1][0] == 0:
        field[len(field) - 1][0] = new_element
    else:
        return


# Grid class to perform moves and add up values if they match
class grid:
    spawnCount = 0
    def __init__(self, current_grid):
        self.current_grid = current_grid
        self.spawnList = [2, 2, 4]



    def move(self, direction):
        def move_row_left(row):
            def tighten(row):  # squeeze non-zero elements together
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        # self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field: \
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: \
            transpose(moves['Right'](transpose(field)))

        if direction in moves:
            # //direction   0: up, 1: right, 2: down, 3: left

            if move_is_possible(direction, self.current_grid):
                self.current_grid = moves[direction](self.current_grid)
                if grid.spawnCount > len(self.spawnList)-1:
                    grid.spawnCount = grid.spawnCount%3
                # print(grid.spawnCount)
                spawn(self.current_grid, self.spawnList, grid.spawnCount)
                grid.spawnCount += 1
                # print(grid.spawnCount)
                return True
            else:
                return False

    def get_current_grid(self):
        return self.current_grid
