import random
from datetime import datetime
import settings


def generateMazeTxt(currentMazeSize, DFS_steps, aStarSteps):
    """ Generate a maze text file
        :return: the maze text file name and the mazeBoard
    """
    newMazeSize = getNewMazeSize(currentMazeSize, DFS_steps, aStarSteps)
    mazeBoard = mazeBoardGenerator(newMazeSize)
    filename = mazeBoardToTxt(mazeBoard)
    print(f" -> New maze of size {newMazeSize}x{newMazeSize} generated")
    return filename, mazeBoard


def getNewMazeSize(currentMazeSize, DFS_steps, aStarSteps, maxMazeSize=settings.MAX_MAZE_SIZE):
    """
        :param maxMazeSize: the maze will never be bigger than the max size
        :param currentMazeSize: the size of the actual maze
        :param DFS_steps: the number of step that the DFS algo took
        :param aStarSteps: the number of step that the aStar algo took
        :return: the next maze size
    """
    if aStarSteps < DFS_steps:
        return min(currentMazeSize + (DFS_steps - aStarSteps), maxMazeSize)  # create a bigger maze (or the max size)
    return currentMazeSize  # else the size will not change


def mazeBoardToTxt(mazeBoard):
    """Create the maze text file
        :param mazeBoard: The board of the maze, it should looks like this : [[201],[100],[030]]
    """
    date = datetime.now().strftime("%I%M%S")
    filename = f"{str(len(mazeBoard))}x{str(len(mazeBoard))}_{date}.txt"

    with open(filename, 'w') as f:
        # change the int to str
        for line in mazeBoard:
            f.write("".join([str(i) for i in line]) + "\n")
    return filename


# Maze generator -- Randomized Prim Algorithm
def mazeBoardGenerator(size, NOTHING=0, WALL=1, START=2, EXIT=3):
    """ Generate a maze that looks like this:
       [[1,2,1,1,1],
        [1,0,0,0,1],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [1,1,1,3,1]]

    :param size: int that define the maze size
    :param NOTHING: will be the char / int of empty tile
    :param WALL: will be the char / int of the wall
    :param START: will be char / int of the end of the maze
    :param EXIT: will be the char / int of the exit
    :return: the maze board list
    """

    # Find number of surrounding cells
    def surroundingCells(rand_wall):
        s_cells = 0
        if (maze[rand_wall[0] - 1][rand_wall[1]] == NOTHING):
            s_cells += 1
        if (maze[rand_wall[0] + 1][rand_wall[1]] == NOTHING):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1] - 1] == NOTHING):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1] + 1] == NOTHING):
            s_cells += 1

        return s_cells

    ## Main code
    # Init variables

    unvisited = 'u'
    height = size
    width = size
    maze = []

    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Randomize starting point and set it a NOTHING
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height - 1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width - 1):
        starting_width -= 1

    # Mark it as NOTHING and add surrounding walls to the list
    maze[starting_height][starting_width] = NOTHING
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height - 1][starting_width] = WALL
    maze[starting_height][starting_width - 1] = WALL
    maze[starting_height][starting_width + 1] = WALL
    maze[starting_height + 1][starting_width] = WALL

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == NOTHING):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = NOTHING

                    # Mark the new walls
                    # Upper NOTHING
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] - 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom NOTHING
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] + 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost NOTHING
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != NOTHING):
                            maze[rand_wall[0]][rand_wall[1] - 1] = WALL
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == NOTHING):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = NOTHING

                    # Mark the new walls
                    # Upper NOTHING
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] - 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost NOTHING
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != NOTHING):
                            maze[rand_wall[0]][rand_wall[1] - 1] = WALL
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost NOTHING
                    if (rand_wall[1] != width - 1):
                        if maze[rand_wall[0]][rand_wall[1] + 1] != NOTHING:
                            maze[rand_wall[0]][rand_wall[1] + 1] = WALL
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height - 1):
            if (maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == NOTHING):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = NOTHING

                    # Mark the new walls
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] + 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != NOTHING):
                            maze[rand_wall[0]][rand_wall[1] - 1] = WALL
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != NOTHING):
                            maze[rand_wall[0]][rand_wall[1] + 1] = WALL
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the right wall
        if (rand_wall[1] != width - 1):
            if (maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == NOTHING):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = NOTHING

                    # Mark the new walls
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != NOTHING):
                            maze[rand_wall[0]][rand_wall[1] + 1] = WALL
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] + 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != NOTHING):
                            maze[rand_wall[0] - 1][rand_wall[1]] = WALL
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = WALL

    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == NOTHING):
            maze[0][i] = START
            break

    for i in range(width - 1, 0, -1):
        if (maze[height - 2][i] == NOTHING):
            maze[height - 1][i] = EXIT
            break
    return maze
