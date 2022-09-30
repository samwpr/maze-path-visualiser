
def DFS(board, startPos, goalPos, ):
    explored = [startPos]
    frontier = [startPos]
    dfsPath = {}
    dSeacrh = []
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSeacrh.append(currCell)
        if currCell == goalPos:
            break
        poss = 0

        directions = {"E": (1, 0), "S": (0, 1), "N": (0, -1), "W": (-1, 0)}
        for d in directions.keys():  # all directions : ESNW
            child = (currCell[0] + directions[d][0], currCell[1] + directions[d][1])  # X, Y pos of the tile in the d direction

            if len(board[0]) > child[0] >= 0 and  len(board) > child[1] >= 0:  # checks if child is valid (not out of range of the board)
                nextTileNb = board[child[1]][child[0]]  # looks what is the number of the child tile
                if nextTileNb != 1:  # if it is not a wall
                    if child in explored:
                        continue
                    poss += 1
                    explored.append(child)
                    frontier.append(child)
                    dfsPath[child] = currCell

    fwdPath = {}
    cell = goalPos
    while cell != startPos:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    exploredTilesPos = dSeacrh
    exploredTilesPos.remove(startPos)
    exploredTilesPos.remove(goalPos)
    solutionsTilesPos = list(fwdPath.values())
    solutionsTilesPos.remove(goalPos)

    return exploredTilesPos, solutionsTilesPos



