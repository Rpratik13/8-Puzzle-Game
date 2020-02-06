from main import final_state

def locatePosition(num):
    for row in range(3):
        for col in range(3):
            if final_state[row][col] == num:
                return [row, col]

class State(object):

    def __init__(self, tl, tm, tr, ml, mm, mr, bl, bm, br):
        self.value = [[tl, tm, tr],
                      [ml, mm, mr],
                      [bl, bm, br]]


    def blankLocation(self):
        for row in range(3):
            for col in range(3):
                if self.value[row][col] == 0:
                    return [row, col]


    def isNotMovable(self, vert, hor, blank):
        if (hor == -1 and blank[1] == 0) or (hor == 1 and blank[1] == 2) or (vert == -1 and blank[0] == 0) or (vert == 1 and blank[0] == 2):
            return True
        return False


    def move(self, vert, hor):
        blank = self.blankLocation()
        if self.isNotMovable(vert, hor, blank):
            return State('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X')
        newState = []
        for row in range(3):
            temp_row = []
            for col in range(3):
                if row == blank[0] and col == blank[1]:
                    temp_row.append(self.value[row + vert][col + hor])
                elif row == blank[0] + vert and col == blank[1] + hor:
                    temp_row.append(self.value[row - vert][col - hor])
                else:
                    temp_row.append(self.value[row][col])
            newState.append(temp_row)
        return State(newState[0][0], newState[0][1], newState[0][2], newState[1][0], newState[1][1], newState[1][2], newState[2][0], newState[2][1], newState[2][2])


    def successors(self):
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        listChild = []
        for move in moves:
            listChild.append(self.move(move[0], move[1]))

        return listChild



    def misplacedTiles(self):
        mTiles = 0
        for row in range(3):
            for col in range(3):
                if self.value[row][col] == 'X':
                    return float('inf')
                elif self.value[row][col] != final_state[row][col]:
                    mTiles += 1
        return mTiles

        
    def manhattanDistance(self):
        mdistance = 0
        
        for row in range(3):
            for col in range(3):
                if self.value[row][col] == 'X':
                    return float('inf')
                elif self.value[row][col] != 0:
                    position = locatePosition(self.value[row][col])
                    mdistance += abs(position[0] - row) + abs(position[1] - col)
        return mdistance


    def isGoalState(self):
        for row in range(3):
            for col in range(3):
                if self.value[row][col] != final_state[row][col]:
                    return False
        return True


    def stateValue(self):
        value = ""
        for row in range(3):
            for col in range(3):
                if self.value[row][col] == 'X':
                    return "{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(self.value[0][0], self.value[0][1], self.value[0][2], self.value[1][0], self.value[1][1], self.value[1][2], self.value[2][0], self.value[2][1], self.value[2][2])

                elif self.value[row][col] == 0:
                    value += '     '
                else:
                    value += str(self.value[row][col]) + "   "
            value += '\n'
        return value
        
    def __repr__(self):
        return "%d| %d| %d\n%d| %d| %d\n%d| %d| %d\n" % (self.value[0][0], self.value[0][1], self.value[0][2], self.value[1][0], self.value[1][1], self.value[1][2], self.value[2][0], self.value[2][1], self.value[2][2])


    def __eq__(self, other):
        for row in range(3):
            for col in range(3):
                if self.value[row][col] != other.value[row][col]:
                    return False
        return True