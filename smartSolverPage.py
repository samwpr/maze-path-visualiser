import generateReport
import gui
import settings
import pygame
import maze
import generateMaze


class SmartSolverPage:
    def __init__(self, screen, mazeGeneratorPage):
        # initialise all the needed variables
        self.showSmartSolverTipsAndTricks = True
        self.screen = screen
        self.mazeGeneratorPage = mazeGeneratorPage
        self.panelInfosParagraph = mazeGeneratorPage.panelInfosParagraph
        self.showSmartSolverTipsAndTricks = True
        self.showMaze = False
        self.maze = None

        # creation of the images
        self.logoImage = gui.Image(screen, "assets/images/Logo.png",
                                   (settings.PANEL_WIDTH // 2, settings.SCREEN_HEIGHT - 110),
                                   size=(249, 135))

        self.dottedGridMImage = gui.Image(screen, "assets/images/Dotted Grid (m).png", (settings.PANEL_WIDTH, 0),
                                          positionType="topleft", size=(918, 680))

        # creation of the texts
        self.titleText = gui.Text(screen, text="Smart Solver", pos=(20, 20), positionType="topleft", fontSize=32,
                                  color=settings.RED)
        self.panelInfosParagraph.addText(None, None, None, None, "", "", "")  # remove the not needed stats

        self.smartSolverTipsAndTricksTitleText = gui.Text(screen, text="Tips & Tricks", pos=(
            settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2, 80),
                                                          positionType="center", fontSize=72,
                                                          color=settings.RED,
                                                          backgroundColor=settings.WHITE)

        self.smartSolverTipsAndTricksParagraph = gui.Paragraph(screen, xPos=settings.PANEL_WIDTH + 95, yStartPos=150,
                                                               fontSize=32, color=settings.LIGHT_RED,
                                                               backgroundColor=settings.WHITE, lineSpacing=77,
                                                               text="1.Click on 'Generate Level From Maze Generator'\n"
                                                                    "2.Next Click 'Solve Level'\n"
                                                                    "3.Choose to see or download the report\n"
                                                                    "4.Go back to the Maze Generator to select another level when you are ready\n"
                                                                    )

        self.gameOverTitleText = gui.Text(screen, text="Game Over", pos=(
            settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2, 200),
                                          positionType="center", fontSize=54, color=settings.LIGHT_RED,
                                          backgroundColor=settings.WHITE)
        self.gameOverText1 = gui.Text(screen, text="Congrats you have completed all levels",
                                      pos=(
                                          settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2,
                                          233),
                                      positionType="center", fontSize=40, color=settings.LIGHT_RED,
                                      backgroundColor=settings.WHITE)
        self.gameOverText2 = gui.Text(screen, text="click on the grey 'Home' button to play the game again",
                                      pos=(
                                          settings.PANEL_WIDTH + (settings.SCREEN_WIDTH - settings.PANEL_WIDTH) // 2,
                                          262),
                                      positionType="center", fontSize=40, color=settings.LIGHT_RED,
                                      backgroundColor=settings.WHITE)

        # creation of the buttons
        # smart solver buttons
        buttonYStartPos = 225  # the first button y position
        buttonsSpaces = 18  # the space between each buttons
        self.generateLevelFromMazeGeneratorButton = gui.Button(screen, pos=(settings.PANEL_WIDTH // 2, buttonYStartPos),
                                                               text="Generate Level From Maze Generator",
                                                               color=settings.LIGHT_RED, fontSize=16, zoomFactor=1)
        self.smartSolverSolveLevelButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces + settings.DEFAULT_BUTTON_SIZE[1]),
                                                      text="Solve Level", color=settings.LIGHT_RED)
        self.showLevelReportButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 2 + settings.DEFAULT_BUTTON_SIZE[1] * 2),
                                                text="Show Level Report", color=settings.LIGHT_RED,
                                                fontSize=22)
        self.downloadLevelReportButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 3 + settings.DEFAULT_BUTTON_SIZE[1] * 3),
                                                    text="Download Level Report", color=settings.LIGHT_RED, fontSize=22)
        self.goMazeGenerator = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 4 + settings.DEFAULT_BUTTON_SIZE[1] * 4),
                                          text="Go Maze Generator", color=settings.LIGHT_RED)
        self.smartSolverHomeButton = gui.Button(screen, pos=(
            settings.PANEL_WIDTH // 2, buttonYStartPos + buttonsSpaces * 5 + settings.DEFAULT_BUTTON_SIZE[1] * 5),
                                                text="Home", color=settings.GRAY)

        self.allButtons = [self.generateLevelFromMazeGeneratorButton, self.smartSolverSolveLevelButton,
                           self.showLevelReportButton, self.downloadLevelReportButton, self.goMazeGenerator,
                           self.smartSolverHomeButton]

    def reset(self):
        """Reset the needed variables"""
        self.showSmartSolverTipsAndTricks = True
        self.showMaze = False
        self.maze = None
        self.panelInfosParagraph.addText(None, None, None, None, None, "", "", "")  # remove the 3 last stats

        for b in self.allButtons:
            b.isSelected = False

        self.scrollYPos = 0
        self.levelReportParagraph = None
        self.levelReportFileName = None
        self.levelReportText = None

    def generateReport(self):
        if self.mazeGeneratorPage.stats[self.mazeGeneratorPage.state] is None:
            stat = {"mazeFileName": self.mazeGeneratorPage.fileName,
                    "mazeNumber": self.mazeGeneratorPage.mazeNumber,
                    "mazeSize": len(self.maze.board),
                    "difficulty": self.mazeGeneratorPage.selectedMazeDifficulty,
                    "DFS_cellsExplored": len(self.mazeGeneratorPage.maze.DFS_exploredTiles),
                    "DFS_solutionPath": len(self.mazeGeneratorPage.maze.DFS_solutionsTiles),
                    "DFS_timeTaken": self.mazeGeneratorPage.maze.animationTime,
                    "aStarCellsExplored": len(self.maze.aStarExploredTiles),
                    "aStarSolutionPath": len(self.maze.aStarSolutionsTiles),
                    "aStarTimeTaken": self.maze.animationTime}

            self.mazeGeneratorPage.stats[self.mazeGeneratorPage.state] = stat

        text, fileName = generateReport.generateReport(self.mazeGeneratorPage.stats)
        reportParagraph = gui.Paragraph(self.screen, xPos=settings.PANEL_WIDTH + 20, yStartPos=20 + self.scrollYPos,
                                        fontSize=24, color=settings.BLACK, lineSpacing=10, text=text)

        self.levelReportText = text
        self.levelReportParagraph = reportParagraph
        self.levelReportFileName = fileName

    def makeReportScroll(self, scrollDirection):
        """
        make the scrolling of the report paragraph
        :param scrollDirection: 1 if scrolling down, -1 if scrolling up, 0 if not scrolling
        """
        self.scrollYPos += scrollDirection * settings.SCROLL_SPEED
        if self.scrollYPos < settings.SCREEN_HEIGHT - self.levelReportParagraph.getLastLineYPos() - 30:
            self.scrollYPos = settings.SCREEN_HEIGHT - self.levelReportParagraph.getLastLineYPos() - 30
        if self.scrollYPos > 0:
            self.scrollYPos = 0

    def run(self, isLeftMouseButtonPressed, scrollDirection):
        # draws the panel in WHITE
        pygame.draw.rect(self.screen, settings.WHITE,
                         (settings.PANEL_WIDTH, 0, settings.SCREEN_WIDTH - settings.PANEL_WIDTH,
                          settings.SCREEN_HEIGHT))
        # draws image
        self.logoImage.draw()

        # draws texts
        self.titleText.draw()
        self.panelInfosParagraph.draw()

        # makes the buttons functional
        # when clicked it will load the maze of the Maze Generator
        if self.generateLevelFromMazeGeneratorButton.run(isLeftMouseButtonPressed) \
                and self.generateLevelFromMazeGeneratorButton.isSelected is False:
            self.maze = maze.Maze(self.screen, self.mazeGeneratorPage.maze.board, self.panelInfosParagraph)
            self.showSmartSolverTipsAndTricks = False
            self.showMaze = True
            self.generateLevelFromMazeGeneratorButton.isSelected = True

        # when clicked it will show how the AStar algo path works
        if self.smartSolverSolveLevelButton.run(isLeftMouseButtonPressed) and self.showMaze \
                and self.smartSolverSolveLevelButton.isSelected is False:
            self.maze.showAStar = True
            self.maze.resetMazeAnimationTimer()
            self.smartSolverSolveLevelButton.isSelected = True

        # when clicked it will create
        if self.showLevelReportButton.run(
                isLeftMouseButtonPressed) and self.maze is not None and self.maze.animationTime is not None \
                and self.showLevelReportButton.isSelected is False:
            self.showMaze = False
            if self.levelReportParagraph is None:
                self.generateReport()
            self.showLevelReportButton.isSelected = True

        # when clicked it will create a text file containing the stats of the maze
        if self.downloadLevelReportButton.run(
                isLeftMouseButtonPressed) and self.maze is not None and self.maze.animationTime is not None \
                and self.downloadLevelReportButton.isSelected is False:
            if self.levelReportParagraph is None:
                self.generateReport()
            generateReport.writeReport(self.levelReportText, self.levelReportFileName)

            self.downloadLevelReportButton.isSelected = True

        # when clicked the user will return to the Maze Generator page in order to load the next maze
        if self.mazeGeneratorPage.state != 3 and self.goMazeGenerator.run(
                isLeftMouseButtonPressed) and self.maze is not None and self.maze.animationTime is not None:
            self.mazeGeneratorPage.reset()
            self.mazeGeneratorPage.mazeNumber += 1  # increase the maze number
            self.mazeGeneratorPage.state += 1
            return "mazeGenerator"

        # when clicked the user will return to the main menu
        if self.smartSolverHomeButton.run(isLeftMouseButtonPressed):
            return "mainMenu"

        # draw the maze when needed
        if self.showMaze and self.maze is not None:
            self.maze.draw()

        # draw the Tip and Tricks when needed
        if self.showSmartSolverTipsAndTricks:
            self.dottedGridMImage.draw()
            self.smartSolverTipsAndTricksTitleText.draw()
            self.smartSolverTipsAndTricksParagraph.draw()

        if self.levelReportParagraph is not None:
            self.makeReportScroll(scrollDirection)
            self.levelReportParagraph.draw(self.scrollYPos)

        if self.mazeGeneratorPage.state == 3 and self.maze is not None and self.maze.animationTime is not None and not self.showLevelReportButton.isSelected:
            self.showSmartSolverTipsAndTricks = False
            self.gameOverTitleText.draw()
            self.gameOverText1.draw()
            self.gameOverText2.draw()
