from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))


def aStar(board, startPos, goalPos):

    open_ = PriorityQueue()
    open_.put((h(startPos, goalPos), h(startPos, goalPos), startPos))
    aPath = {}
    # for each tile position define the score
    g_score = {}
    for lineNb, line in enumerate(board):
        for colNb, tile in enumerate(line):
            if tile != 1:  # if the tile is not a wall
                g_score[(colNb, lineNb)] = float("inf")

    g_score[startPos] = 0

    # for each tile position define the score
    f_score = {}
    for lineNb, line in enumerate(board):
        for colNb, tile in enumerate(line):
            if tile != 1:  # if the tile is not a wall
                f_score[(colNb, lineNb)] = float("inf")
    f_score[startPos] = h(startPos, goalPos)
    searchPath = []
    while not open_.empty():
        currCell = open_.get()[2]
        searchPath.append(currCell)
        if currCell == goalPos:
            break
        directions = {"E": (1, 0), "S": (0, 1), "N": (0, -1), "W": (-1, 0)}
        for d in directions.keys():  # all directions : ESNW
            childCell = (currCell[0] + directions[d][0], currCell[1] + directions[d][1])  # X, Y pos of the tile in the d direction
            if len(board[0]) > childCell[0] >= 0 and  len(board) > childCell[1] >= 0:  # checks if child is valid (not out of range of the board)
                nextTileNb = board[childCell[1]][childCell[0]]  # looks what is the number of the child tile
                if nextTileNb != 1:
                    temp_g_score = g_score[currCell] + 1
                    temp_f_score = temp_g_score + h(childCell, goalPos)

                    if temp_f_score < f_score[childCell]:
                        aPath[childCell] = currCell
                        g_score[childCell] = temp_g_score
                        f_score[childCell] = temp_g_score + h(childCell, goalPos)
                        open_.put((f_score[childCell], h(childCell, goalPos), childCell))

    fwdPath = {}
    cell = goalPos
    while cell != startPos:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    exploredTilesPos = searchPath
    exploredTilesPos.remove(startPos)
    exploredTilesPos.remove(goalPos)

    solutionsTilesPos = list(fwdPath.values())
    solutionsTilesPos.remove(goalPos)

    return exploredTilesPos, solutionsTilesPos




