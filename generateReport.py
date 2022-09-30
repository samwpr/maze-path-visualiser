from datetime import datetime
from generateMaze import getNewMazeSize


def generateReport(stats):
    """Generate a txt file that contain the maze / DFS / aStar stats """
    # define the current maze level number
    if stats[3] is not None:
        currentLevelNb = 3
    elif stats[2] is not None:
        currentLevelNb = 2
    else:
        currentLevelNb = 1

    # define the file name
    date = datetime.now().strftime("%d-%m_%I-%M-%S-%p")
    filename = f"{stats[currentLevelNb]['mazeNumber']}_{date}.txt"
    text = f"Report Name: {filename}\n\n"

    # Versus
    if currentLevelNb > 1:
        # maze generator vs text
        DFS_vsExploredDiffValue = stats[currentLevelNb]['DFS_cellsExplored'] - stats[currentLevelNb - 1]['DFS_cellsExplored']
        DFS_vsSolutionDiffValue = stats[currentLevelNb]['DFS_solutionPath'] - stats[currentLevelNb-1]['DFS_solutionPath']
        DFS_vsExploredDiffPercent = round((stats[currentLevelNb]['DFS_cellsExplored'] - stats[currentLevelNb-1]['DFS_cellsExplored']) / (stats[currentLevelNb-1]['DFS_cellsExplored']/100), 2)
        DFS_vsSolutionDiffPercent = round((stats[currentLevelNb]['DFS_solutionPath'] - stats[currentLevelNb - 1]['DFS_solutionPath']) / (
                    stats[currentLevelNb - 1]['DFS_solutionPath'] / 100), 2)

        text += f"Maze Number {currentLevelNb-1} vs Maze Number {currentLevelNb}\n" \
                f"\n" \
                f"MAZE GENERATOR\n" \
                f"Stats of Maze Generator (DFS) For Maze {currentLevelNb-1}\n" \
                f"Cells Explored: {stats[currentLevelNb-1]['DFS_cellsExplored']}\n" \
                f"Solution Path: {stats[currentLevelNb-1]['DFS_solutionPath']}\n" \
                f"Time Taken: {stats[currentLevelNb-1]['DFS_timeTaken']}sec\n" \
                f"\n" \
                f"Stats of Maze Generator (DFS) For Maze {currentLevelNb}\n" \
                f"Cells Explored: {stats[currentLevelNb]['DFS_cellsExplored']}\n" \
                f"Solution Path: {stats[currentLevelNb]['DFS_solutionPath']}\n" \
                f"Time Taken: {stats[currentLevelNb]['DFS_timeTaken']}sec\n" \
                f"\n" \
                f"Difficulty Maze {currentLevelNb-1} vs Maze {currentLevelNb}\n" \
                f"Cells Explored: {'+' if DFS_vsExploredDiffValue > 0 else ''}{DFS_vsExploredDiffValue}, " \
                f"{'+' if DFS_vsExploredDiffPercent > 0 else ''}{DFS_vsExploredDiffPercent}%\n" \
                f"Solution Path: {'+' if DFS_vsSolutionDiffValue > 0 else ''}{DFS_vsSolutionDiffValue}, " \
                f"{'+' if DFS_vsSolutionDiffPercent > 0 else ''}{DFS_vsSolutionDiffPercent}%\n" \
                f"--------------------------------------------------\n\n"

        # smart solver vs text
        ASTAR_vsExploredDiffValue = stats[currentLevelNb]['aStarCellsExplored'] - stats[currentLevelNb-1]['aStarCellsExplored']
        ASTAR_vsSolutionDiffValue = stats[currentLevelNb]['aStarSolutionPath']-stats[currentLevelNb-1]['aStarSolutionPath']
        AStar_vsExploredDiffPercent = round((stats[currentLevelNb]['aStarCellsExplored'] - stats[currentLevelNb-1]['aStarCellsExplored']) /
                                     (stats[currentLevelNb-1]['aStarCellsExplored']/100), 2)
        AStar_vsSolutionDiffPercent = round((stats[currentLevelNb]['aStarSolutionPath'] - stats[currentLevelNb - 1]['aStarSolutionPath']) /
                                     (stats[currentLevelNb - 1]['aStarSolutionPath'] / 100), 2)

        text += f"SMART SOLVER\n" \
                f"Stats of Smart Solver (A Star) For Maze {currentLevelNb-1}\n" \
                f"Cells Explored: {stats[currentLevelNb-1]['aStarCellsExplored']}\n" \
                f"Solution Path: {stats[currentLevelNb-1]['aStarSolutionPath']}\n" \
                f"Time Taken: {stats[currentLevelNb-1]['aStarTimeTaken']}sec\n" \
                f"\n" \
                f"Stats of Maze Generator (DFS) For Maze {currentLevelNb}\n" \
                f"Cells Explored: {stats[currentLevelNb]['aStarCellsExplored']}\n" \
                f"Solution Path: {stats[currentLevelNb]['aStarSolutionPath']}\n" \
                f"Time Taken: {stats[currentLevelNb]['aStarTimeTaken']}sec\n" \
                f"\n" \
                f"Difficulty Maze {currentLevelNb-1} vs Maze {currentLevelNb}\n" \
                f"Cells Explored: {'+' if ASTAR_vsExploredDiffValue > 0 else ''}{ASTAR_vsExploredDiffValue}, " \
                f"{'+' if AStar_vsExploredDiffPercent > 0 else ''}{AStar_vsExploredDiffPercent}%\n" \
                f"Solution Path: {'+' if ASTAR_vsSolutionDiffValue > 0 else ''}{ASTAR_vsSolutionDiffValue}, " \
                f"{'+' if AStar_vsSolutionDiffPercent > 0 else ''}{AStar_vsSolutionDiffPercent}%\n" \
                f"--------------------------------------------------\n\n"

    # add the current maze stats
    text += f"Maze Number: {stats[currentLevelNb]['mazeNumber']}\n" \
           f"Maze Size: {stats[currentLevelNb]['mazeSize']}x{stats[currentLevelNb]['mazeSize']}\n" \
           f"Maze File Name: {stats[currentLevelNb]['mazeFileName']}.txt\n" \
           f"\n" \
           f"of Maze Generator (DFS)\n" \
           f"Cells Explored: {stats[currentLevelNb]['DFS_cellsExplored']}\n" \
           f"Solution Path: {stats[currentLevelNb]['DFS_solutionPath']}\n" \
           f"Time Taken: {stats[currentLevelNb]['DFS_timeTaken']}sec\n" \
           f"\n" \
           f"Stats of Smart Solver (A Star)\n" \
           f"Cells Explored: {stats[currentLevelNb]['aStarCellsExplored']}\n" \
           f"Solution Path: {stats[currentLevelNb]['aStarSolutionPath']}\n" \
           f"Time Taken: {stats[currentLevelNb]['aStarTimeTaken']}sec\n" \
           f"\n" \
           f"Efficiency of Cells Explored by Smart Solver Compared to Maze Generator: {round((stats[currentLevelNb]['DFS_cellsExplored'] - stats[currentLevelNb]['aStarCellsExplored']) / stats[currentLevelNb]['DFS_cellsExplored'] * 100, 2)}%\n\n" \
           f"Efficiency of Solution Path by Smart Solver Compared to Maze Generator: {round((stats[currentLevelNb]['DFS_solutionPath'] - stats[currentLevelNb]['aStarSolutionPath']) / stats[currentLevelNb]['DFS_solutionPath'] * 100, 2)}%\n"

    if stats[currentLevelNb]['aStarCellsExplored'] < stats[currentLevelNb]['DFS_cellsExplored']:
        # nextMazeSize = getNewMazeSize(mazeSize, DFS_cellsExplored, aStarCellsExplored)
        text += "\n\nSeeing that the cells explored by the Smart Solver takes less steps\n" \
                "we should increase the difficulty of the maze but at the same\n" \
                "time making it a maze that can be solved by the maze generator\n\n"\
                "Increase Difficulty"
    else:
        text += "\nSeeing the cells explored by the Smart Solver did not out preforming the maze\n" \
                "generator we recommended generating a new maze of the\n" \
                "same difficulty to train the smart solver\n\n"\
                "Same or Decrease Difficulty"

    return text, filename


def writeReport(text, filename):
    with open(filename, 'w') as f:
        f.write(text)
    print(f" -> Report with the name {filename} generated")
