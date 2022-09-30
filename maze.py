import pygame
import time
import settings
from DFS_for_maze import DFS
from aStar_for_maze import aStar


class Maze:
    def __init__(self, surface, board, panelInfosParagraph):
        self.surface = surface
        self.board = board  # a board looks like this : [[1,1,0], [0,1,2],[3,0,0]]
        self.panelInfosParagraph = panelInfosParagraph
        self.show = False
        mazeBorderSpace = 20  # the border size between the screen top and maze top, and the screen bottom and maze bottom
        self.mazeSize = min(settings.SCREEN_WIDTH - settings.PANEL_WIDTH - 2 * mazeBorderSpace,
                            settings.SCREEN_HEIGHT - 2 * mazeBorderSpace)
        self.tileSize = self.mazeSize // len(self.board)
        self.linesWidth = 2
        self.linesColor = settings.BLACK

        # find the start and end pos and solve the maze with DFS and aStar
        startPos, endPos = self.startEndTilePos()
        self.DFS_exploredTiles, self.DFS_solutionsTiles = DFS(self.board, startPos, endPos)
        self.DFS_solutionsTiles = self.DFS_solutionsTiles[::-1]  # reverse the order so it start from the start cell
        self.showDFS = False
        self.aStarExploredTiles, self.aStarSolutionsTiles = aStar(self.board, startPos, endPos)
        self.aStarSolutionsTiles = self.aStarSolutionsTiles[::-1]  # reverse the order so it start from the start cell
        self.showAStar = False

        self.mazeAnimationTimer = None
        self.startAnimationTime = None
        self.currentAnimationStep = None
        self.animationTime = None  # the time that the animation has taken

    def startEndTilePos(self):
        """ Find the start pos and end pos
            :return: the start pos and end pos tile position of the maze
        """
        startPos = None
        endPos = None
        for lineNb, line in enumerate(self.board):
            for colNb, tile in enumerate(line):
                if tile == 2:
                    startPos = (colNb, lineNb)
                elif tile == 3:
                    endPos = (colNb, lineNb)
        if startPos is None or endPos is None:
            print("You have to define the start pos and end pos!")
        return startPos, endPos

    def resetMazeAnimationTimer(self):
        self.startAnimationTime = self.mazeAnimationTimer = time.time()
        self.currentAnimationStep = 0
        self.animationTime = None

    def runAnimation(self):
        """makes the path animation work"""
        if self.showDFS or self.showAStar:
            # define if it will show the DFS or AStar
            if self.showDFS:
                exploredTiles = self.DFS_exploredTiles
                solutionsTiles = self.DFS_solutionsTiles
            else:
                exploredTiles = self.aStarExploredTiles
                solutionsTiles = self.aStarSolutionsTiles
            while time.time() > self.mazeAnimationTimer + settings.MAZE_ANIMATION_SPEED:
                self.mazeAnimationTimer += settings.MAZE_ANIMATION_SPEED
                self.currentAnimationStep += 1
                if self.currentAnimationStep == len(exploredTiles) + len(solutionsTiles):
                    self.animationTime = round(time.time() - self.startAnimationTime, 1)
                    # update the maze info panel
                    self.panelInfosParagraph.addText(None, None, None, None, None, len(exploredTiles),
                                                     len(solutionsTiles), str(self.animationTime) + "sec")

    def draw(self, drawSolutionPath=True, drawExploredPath=True):
        """ Center the maze, draw every tile and draw the grid"""
        self.runAnimation()

        mazeXStartPos = settings.PANEL_WIDTH + (
                settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2 - self.mazeSize // 2  # the X position of the top left tile
        mazeYStartPos = settings.SCREEN_HEIGHT // 2 - self.mazeSize // 2  # the y position of the top left tile

        # draw the tiles
        for lineNb, line in enumerate(self.board):
            yPos = mazeYStartPos + lineNb * self.tileSize
            for colNb, tile in enumerate(line):
                xPos = mazeXStartPos + colNb * self.tileSize
                color = settings.MAZE_COLOR[tile]
                # checks if the tile is in the solution path and if the explored tile animation is ended
                if self.showDFS or self.showAStar:
                    # define if it will show the DFS or AStar
                    if self.showDFS:
                        exploredTiles = self.DFS_exploredTiles
                        solutionsTiles = self.DFS_solutionsTiles
                    else:
                        exploredTiles = self.aStarExploredTiles
                        solutionsTiles = self.aStarSolutionsTiles

                    if (colNb, lineNb) in solutionsTiles[
                                                           :self.currentAnimationStep - len(exploredTiles)] \
                            and (self.currentAnimationStep - len(exploredTiles)) > 0:
                        if drawSolutionPath:
                            color = settings.YELLOW
                    # checks if the tile has been explored by DFS
                    elif (colNb, lineNb) in exploredTiles[:self.currentAnimationStep]:
                        if drawExploredPath:
                            color = settings.LIGHT_BLUE
                pygame.draw.rect(self.surface, color, (xPos, yPos, self.tileSize, self.tileSize))

        # draw the grid
        for nb in range(len(self.board) + 1):
            # draw the horizontal lines
            yPos = mazeYStartPos + nb * self.tileSize
            pygame.draw.line(self.surface, self.linesColor, (mazeXStartPos, yPos),
                             (mazeXStartPos + self.tileSize * len(self.board), yPos), self.linesWidth)
            # draw the vertical lines
            xPos = mazeXStartPos + nb * self.tileSize
            pygame.draw.line(self.surface, self.linesColor, (xPos, mazeYStartPos),
                             (xPos, mazeYStartPos + self.tileSize * len(self.board)), self.linesWidth)

